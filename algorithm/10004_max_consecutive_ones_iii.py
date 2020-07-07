"""
题目：https://leetcode-cn.com/problems/max-consecutive-ones-iii/

给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。

返回仅包含 1 的最长（连续）子数组的长度。

 

示例 1：

输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释： 
[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。
示例 2：

输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。
 

提示：

1 <= A.length <= 20000
0 <= K <= A.length
A[i] 为 0 或 1
"""

import time
from typing import List


class Solution1:
    """
    暴力法：从每个元素开始，往后找能最大到的最远位置，然后获取最大值
    """
    def longestOnes(self, A: List[int], K: int) -> int:
        lenA = len(A)
        ans = 0

        if K >= lenA: return lenA

        for i in range(lenA):
            tmpSum = 0
            for j in range(i, lenA):
                tmpSum += A[j]
                if tmpSum + K < j - i + 1:
                    break
                ans = max(ans, j - i + 1)
        return ans


if __name__ == "__main__":
    test = [
        [[1,1,1,0,0,0,1,1,1,1,0], 2], # 6
        [[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3], # 10
    ]
    start = time.perf_counter()
    for (A, K) in test:
        result = Solution1().longestOnes(A, K)
        print(f'A: {A}; K:{K}; result: {result}')
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
