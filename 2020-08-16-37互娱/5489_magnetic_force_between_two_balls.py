"""
题目：在代号为 C-137 的地球上，Rick 发现如果他将两个球放在他新发明的篮子里，它们之间会形成特殊形式的磁力。Rick 有 n 个空的篮子，第 i 个篮子的位置在 position[i] ，Morty 想把 m 个球放到这些篮子里，使得任意两球间 最小磁力 最大。
已知两个球如果分别位于 x 和 y ，那么它们之间的磁力为 |x - y| 。
给你一个整数数组 position 和一个整数 m ，请你返回最大化的最小磁力。


示例 1：
输入：position = [1,2,3,4,7], m = 3
输出：3
解释：将 3 个球分别放入位于 1，4 和 7 的三个篮子，两球间的磁力分别为 [3, 3, 6]。最小磁力为 3 。我们没办法让最小磁力大于 3 。

示例 2：
输入：position = [5,4,3,2,1,1000000000], m = 2
输出：999999999
解释：我们使用位于 1 和 1000000000 的篮子时最小磁力最大。
"""

import time
from typing import List
import sys


class Solution1:
    """
    题目转化为求解一个有序数组进行分组成 m-1 个连续子数组，求解各个子数组首尾两个元素之差，差值最大化的情况下，求解子数组中元素之差的最小值
    dp[i][j] 表示i个篮子分成j组，这j组的子数组中收尾元素的之差
    """
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        # sub[i] - sub[j] 用于存储排序后的篮子，第i个篮子与第j个篮子之间的引力
        sub = [0] + position
        # 初始化状态转移方程
        n = len(position)
        dp = [[float('inf')] * m for _ in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, min(i, m)):
                for k in range(2, i + 1):
                    if dp[i][j] == float('inf'):
                        dp[i][j] = min(dp[k][j - 1], sub[i] - sub[k])
                    else:
                        dp[i][j] = max(dp[i][j], min(dp[k][j - 1], sub[i] - sub[k - 1]))
                    # dp[i][j] = max(dp[i][j], min(dp[k][j - 1], sub[i] - sub[k]))
        for i in dp:
            print(f'{i}')
        return dp[n][m - 1]


class Solution2:
    """
    二分查找，需要具有单调性的特征的问题，分析解答结果：最小值即为有序数组的相邻元素之差的最小值；最大值即为有序数组的首尾元素之差
    为了缩短计算范围，这里的最大值，降低为 `(首尾元素之差) / 分组个数`
    """
    def maxDistance(self, position: List[int], m: int) -> int:
        def check(num):
            """ 
            判断 子数组距离最小值为num 的子数组个数是否大于等于 m 
            概念：子数组距离指的是子数组的最后一个元素与第一个元素之差
            """
            cnt = 1
            startPosition = position[0]
            for item in position:
                if item - startPosition >= num:
                    cnt += 1
                    startPosition = item
                    if cnt >= m: break
            return cnt >= m

        if len(position) < 2 or m < 2: return 0

        position.sort()
        lenPosition = len(position)
        left = min([position[i + 1] - position[i] for i in range(lenPosition - 1)])
        right = (position[-1] - position[0]) // (m - 1)

        # while left <= right:
        #     mid = (left + right) // 2
        #     if check(mid):
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        #     # print(f'{left} {right}')

        # while left < right:
        #     mid = (left + right) // 2
        #     if check(mid):
        #         left = mid + 1
        #     else:
        #         right = mid

        while left <= right:
            mid = left + ((right - left) >> 1)
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left - 1



if __name__ == "__main__":
    test = [
        [[1,2,3,4,7], 3],  # 3
        [[79,74,57,22], 4],  # 5
        [[5,4,3,2,1,1000000000], 2],  # 999999999
    ]
    start = time.perf_counter()
    for position, m in test:
        result = Solution2().maxDistance(position, m)
        print(f'position = {position}, m = {m} => maxDistance = {result}')
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
