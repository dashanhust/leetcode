"""
题目：https://leetcode-cn.com/problems/subarrays-with-k-different-integers/

给定一个正整数数组 A，如果 A 的某个子数组中不同整数的个数恰好为 K，则称 A 的这个连续、不一定独立的子数组为好子数组。
（例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。）
返回 A 中好子数组的数目。

示例 1：
输入：A = [1,2,1,2,3], K = 2
输出：7
解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].

示例 2：
输入：A = [1,2,1,3,4], K = 3
输出：3
解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].
 
提示：
1 <= A.length <= 20000
1 <= A[i] <= A.length
1 <= K <= A.length
"""

import time
from typing import List
from collections import defaultdict



class Solution1:
    """
    暴力解法
    判断每个子串是否是符合要求的
    """
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        # ans = []
        distance = 0
        lenA = len(A)
        window = defaultdict(int)
        for left in range(lenA):
            for right in range(left + 1, lenA + 1):
                window = A[left:right]
                if len(set(window)) == K:
                    # ans.append(window)
                    distance += 1
        return distance

class Solution2:
    """
    采用滑动窗口来解决
    当窗口的互异元素个数为K时，就需要获取已right下标结尾的元素的长度也为K的数量，然后将窗口还原
    """
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        left, right, distance = 0, 0, 0
        window = defaultdict(int)
        lenA = len(A)
        # ans = []

        while right < lenA:
            # 右边元素移入窗口
            c = A[right]
            right += 1
            # 窗口元素处理，使得窗口的长度等于K
            window[c] += 1
            while len(window) > K:
                d = A[left]
                left += 1
                window[d] -= 1
                if window[d] == 0:
                    del window[d]
            
            # 是否收敛窗口
            tmp = left
            while len(window) == K:
                # ans.append(A[tmp:right])
                distance += 1
                # 左边元素移出窗口
                d = A[tmp]
                tmp += 1
                window[d] -= 1
                if window[d] == 0:
                    del window[d]

            # 还原窗口
            while tmp > left:
                d = A[tmp - 1]
                window[d] += 1
                tmp -= 1
                
        return distance


if __name__ == "__main__":
    test = [
        [[1,2,1,2,3], 2], # 7
        [[1,2,1,3,4], 3], # 3
    ]
    start = time.perf_counter()
    for (A, K) in test:
        result = Solution2().subarraysWithKDistinct(A, K)
        print(f'A: {A}; K: {K}; result: {result}')
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
