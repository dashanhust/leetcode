"""
题目：几块石子 排成一行 ，每块石子都有一个关联值，关联值为整数，由数组 stoneValue 给出。

游戏中的每一轮：Alice 会将这行石子分成两个 非空行（即，左侧行和右侧行）；Bob 负责计算每一行的值，即此行中所有石子的值的总和。Bob 会丢弃值最大的行，Alice 的得分为剩下那行的值（每轮累加）。如果两行的值相等，Bob 让 Alice 决定丢弃哪一行。下一轮从剩下的那一行开始。

只 剩下一块石子 时，游戏结束。Alice 的分数最初为 0 。

返回 Alice 能够获得的最大分数 。


示例 1：
输入：stoneValue = [6,2,3,4,5,5]
输出：18
解释：在第一轮中，Alice 将行划分为 [6，2，3]，[4，5，5] 。左行的值是 11 ，右行的值是 14 。Bob 丢弃了右行，Alice 的分数现在是 11 。
在第二轮中，Alice 将行分成 [6]，[2，3] 。这一次 Bob 扔掉了左行，Alice 的分数变成了 16（11 + 5）。
最后一轮 Alice 只能将行分成 [2]，[3] 。Bob 扔掉右行，Alice 的分数现在是 18（16 + 2）。游戏结束，因为这行只剩下一块石头了。

示例 2：
输入：stoneValue = [7,7,7,7,7,7,7]
输出：28

示例 3：
输入：stoneValue = [4]
输出：0

提示：
1 <= stoneValue.length <= 500
1 <= stoneValue[i] <= 10^6
"""

import time
from typing import List


class Solution1:
    """
    根据题目得知石头的数量比较有限，只有500个，所以我们可以采用动态规划的思路才求解
    dp(i, j) 表示第 i 个石头到第 j 个石头之间，这个子数组，根据题目的方式，能够获得的最大分数
    若stoneValue[i:j+1]的最佳划分点为k, (i <= k < j)，则有

    dp(i, j) = max(dp(i, k) + sum(i, k), dp(k+1, j) + sum(k+1, j))

    其中 sum(i,k) 表示第k个石头和第i个石头之间的数值之和(不包括石头i)，可以标记为 sumStone(k) - sumStone(i - 1) 其中 sumStone(i) 表示stoneValue数组前i个石头数值之和

    时间复杂度: O(n^2)
    空间复杂度: O(n^2)
    """
    def stoneGameV(self, stoneValue: List[int]) -> int:
        def helper(i, j):
            if dp[i][j] != -1: return dp[i][j]

            result = 0
            for k in range(i, j):
                tmp = 0
                leftSum = sumStone[k] - sumStone[i - 1]
                rightSum = sumStone[j] - sumStone[k]
                if leftSum < rightSum:
                    tmp = leftSum + helper(i, k)
                elif leftSum > rightSum:
                    tmp = rightSum + helper(k + 1, j)
                else:
                    tmp = max(leftSum + helper(i, k), rightSum + helper(k + 1, j))
                result = max(result, tmp)
            dp[i][j] = result
            return result


        if len(stoneValue) <= 1: return 0

        lenStone = len(stoneValue)
        dp = [[-1] * (lenStone + 1) for _ in range(lenStone + 1)]
        sumStone = [0]
        for idx, item in enumerate(stoneValue):
            sumStone.append(sumStone[-1] + item)
        return helper(1, lenStone)


if __name__ == "__main__":
    test = [
        [6,2,3,4,5,5],  # 18
        [7,7,7,7,7,7,7],  # 28
        [4],  # 0
        [10,9,8,7,6,5,4,3,2,1],  # 37
    ]
    start = time.perf_counter()
    for item in test:
        result = Solution1().stoneGameV(item)
        print(f'{item} => {result}')
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
