"""
题目：https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/

给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

示例 1:

输入:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出: 3
解释: 
长度最长的公共子数组是 [3, 2, 1]。
说明:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
"""

import time
from typing import List
import collections


class Solution1:
    """
    暴力法：遍历数组A的所有子数组，在B中是否存在，如果存在，那么统计该子数组的长度是否大于已经统计的子数组的长度
    """
    def findLength(self, A: List[int], B: List[int]):
        subArray = []
        lenA = len(A)
        lenB = len(B)

        for i in range(lenA):
            for j in range(i, lenA):
                # 检查A[i:j]是否在B中存在，如果存在的话，那么就判断subArray的长度 
                tmpA = A[i:j + 1]
                for k in range(lenB - len(tmpA) + 1):
                    l = 0
                    m = k
                    while l < len(tmpA) and tmpA[l] == B[m]:
                        l += 1
                        m += 1
                    if l == len(tmpA) and len(tmpA) > len(subArray):
                        subArray = tmpA
                        
        return len(subArray)


class Solution2:
    """
    穷举法： 穷举数组A的起始位置i和数组B的起始位置j，随后超出最大值k满足 A[i:i+k] == B[j:j+k]
    """
    def findLength(self, A: List[int], B: List[int]) -> int:
        lenA = len(A)
        lenB = len(B)
        ans = 0

        for i in range(lenA):
            for j in range(lenB):
                k = 0
                while i + k < lenA and j + k < lenB and A[i + k] == B[j + k]:
                    k += 1
                ans = max(ans, k) 
        return ans


class Solution3:
    """
    穷举法 + 哈希表： 时间复杂度为 O(lenA * lenB * min(lenA, lenB))
    同Solution2中的穷举法，但是在判断相等的时候，这里引入了字典来存储相同字段的出现索引位置，尽量减少轮训的次数
    """
    def findLength(self, A: List[int], B: List[int]) -> int:
        # 保证A是大数组，B是小数组
        if len(A) < len(B):
            A, B = B, A
        
        lenA = len(A)
        lenB = len(B)
        ans = 0
        Bstarts = collections.defaultdict(list)
        for idx, item in enumerate(B):
            Bstarts[item].append(idx)

        for i in range(lenA):
            Bindexes = Bstarts[A[i]]
            for j in Bindexes:
                k = 0
                while i + k < lenA and j + k < lenB and A[i + k] == B[j + k]:
                    k += 1
                ans = max(ans, k)
        return ans


class Solution4:
    """
    动态规划 时间复杂度为 O(lenA * lenB)
    参考: https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/solution/zui-chang-zhong-fu-zi-shu-zu-by-leetcode/
         https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/solution/zhe-yao-jie-shi-ken-ding-jiu-dong-liao-by-hyj8/

    设dp[i][j] 为A[:i+1]和B[:j+1]以A[i]和B[j]结尾的公共最长公共前缀，那么答案就位所有dp[i][j]中的最大值max(dp[i][j])
    例如 dp[4][5] 就表示A[:4]和B[:5]数组中以A[3]和B[4]相等情况下结尾的公共子数组的最大长度
    若 A[:4] = [1, 2, 3, 4]
       B[:5] = [1, 2, 3, 4, 5]
    由于 A[3] = 4 而 B[4] = 5 两者不相同，所以两者的最长公共子数组长度为 0 则 dp[4, 5] = 0
    而若 B[:5] = [1, 2, 3, 4, 4] 由于 A[3] == B[4] 那么已 4 结尾的公共子数组长度为 1 则 dp[4, 5] = 1

    那么状态转移方程为：
    当 A[i] == B[j]: dp[i][j] = dp[i - 1][j - 1] + 1
    当 A[i] != B[j]: dp[i][j] = 0
    """
    def findLength(self, A: List[int], B: List[int]) -> int:
        lenA = len(A)
        lenB = len(B)
        ans = 0
        
        dp = [[0] * (lenB + 1) for _ in range(lenA + 1)]
        for i in range(1, lenA + 1):
            for j in range(1, lenB + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
            ans = max(*dp[i], ans)
        return ans


class Solution5:
    """
    动态规划的空间利用率优化
    Solution4的动态规划做法，已经很好的优化了时间效率，但是空间效率没有进行优化，我们这里可以进行优化。
    因为根据状态转移方程，其实每次计算 dp[i][j] 的时候，实际上只是使用了dp[i-1][j-1]，也就是dp数组的上一行，所以我们可以只使用一行数组，然后对这个数组进行更新即可
    """
    def findLength(self, A: List[int], B: List[int]) -> int:
        lenA = len(A)
        lenB = len(B)
        ans = 0

        dp = [0] * (lenB + 1)
        for i in range(1, lenA + 1):
            for j in range(lenB, 0, -1):
                if A[i - 1] == B[j - 1]:
                    dp[j] = dp[j - 1] + 1
                else:
                    dp[j] = 0
            ans = max(*dp, ans)
        return ans


class Solution6:
    """
    滑动窗口： 时间复杂度 O((lenA + lenB) * min(lenA + lenB))
    参考 https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/solution/zui-chang-zhong-fu-zi-shu-zu-by-leetcode-solution/
    表示设置A和B数组的首元素，然后依次比较两个数组的第二个元素，第三个元素...也就是比较相同下表的数据，如果相等，那么相同子数组长度加1，否则置为0，这样就得到了已某个数组开头的最大子数组个数
    """
    def findLength(self, A: List[int], B: List[int]) -> int:
        def maxLength(addA: int, addB: int, length: int) -> int:
            ret = tmp = 0
            for i in range(length):
                if A[addA + i] == B[addB + i]:
                    tmp += 1
                    ret = max(ret, tmp)
                else:
                    tmp = 0
            return ret

        lenA = len(A)
        lenB = len(B)
        ans = 0
        # A数组不动，依次移动数组B来与数组A对齐比较
        for i in range(lenB):
            length = min(lenA, lenB - i)
            ret = maxLength(0, i, length)
            ans = max(ret, ans)
        # B数组不动，依次移动数组A来与数组B对齐比较
        for i in range(lenA):
            length = min(lenA - i, lenB)
            ret = maxLength(i, 0, length)
            ans = max(ret, ans)
        return ans


if __name__ == "__main__":
    test = [
        [
            [1,2,3,2,1],
            [3,2,1,4,7]
        ], # 3 [3, 2, 1]
        [
            [0,0,0,0,0],
            [0,0,0,0,0]
        ], # 5 [0,0,0,0,0]
        [
            [0,0,0,0,1],
            [1,0,0,0,0]
        ], # 4 [0, 0, 0, 0]
        [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ]
    ]
    start = time.perf_counter()
    for (a, b) in test:
        result = Solution6().findLength(a, b)
        # print(f'{a} {b} maximum length of repeated subarray: {result}')
        print(f'maximum length of repeated subarray: {result}')
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
