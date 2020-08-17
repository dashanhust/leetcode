"""
题目：厨房里总共有 n 个橘子，你决定每一天选择如下方式之一吃这些橘子：

吃掉一个橘子。
如果剩余橘子数 n 能被 2 整除，那么你可以吃掉 n/2 个橘子。
如果剩余橘子数 n 能被 3 整除，那么你可以吃掉 2*(n/3) 个橘子。
每天你只能从以上 3 种方案中选择一种方案。

请你返回吃掉所有 n 个橘子的最少天数。


示例 1：
输入：n = 10
输出：4
解释：你总共有 10 个橘子。
第 1 天：吃 1 个橘子，剩余橘子数 10 - 1 = 9。
第 2 天：吃 6 个橘子，剩余橘子数 9 - 2*(9/3) = 9 - 6 = 3。（9 可以被 3 整除）
第 3 天：吃 2 个橘子，剩余橘子数 3 - 2*(3/3) = 3 - 2 = 1。
第 4 天：吃掉最后 1 个橘子，剩余橘子数 1 - 1 = 0。
你需要至少 4 天吃掉 10 个橘子。

示例 2：
输入：n = 6
输出：3
解释：你总共有 6 个橘子。
第 1 天：吃 3 个橘子，剩余橘子数 6 - 6/2 = 6 - 3 = 3。（6 可以被 2 整除）
第 2 天：吃 2 个橘子，剩余橘子数 3 - 2*(3/3) = 3 - 2 = 1。（3 可以被 3 整除）
第 3 天：吃掉剩余 1 个橘子，剩余橘子数 1 - 1 = 0。
你至少需要 3 天吃掉 6 个橘子。

示例 3：
输入：n = 1
输出：1

示例 4：
输入：n = 56
输出：6

提示：
1 <= n <= 2*10^9
"""

import time
from typing import List


class Solution1:
    """
    采用数组法，将从 1到n 的情况下，结果都给计算出来，从而求解出最终结果。
    """
    def minDays(self, n: int) -> int:
        storeDays = [0]
        for i in range(1, n + 1):
            tmp = storeDays[i - 1] + 1
            if i & 1 == 0:
                tmp = min(tmp, storeDays[i // 2] + 1)
            if i % 3 == 0:
                tmp = min(tmp, storeDays[i // 3] + 1)
            storeDays.append(tmp)
        return storeDays[-1]


class Solution2:
    def minDays(self, n: int) -> int:
        q = [n]
        d = dict()
        d[n] = 0
        while 0 not in d:
            v = q.pop(0)
            dv = d[v]
            if v % 3 == 0 and v // 3 not in d:
                d[v // 3] = d[v] + 1
                q.append(v // 3)
            if v % 2 == 0 and v // 2 not in d:
                d[v // 2] = d[v] + 1
                q.append(v // 2)
            if v - 1 not in d:
                d[v - 1] = d[v] + 1
                q.append(v - 1)
        return d[0]


class Solution3:
    """
    采用递归的方法，并且不用去判断是否能够被 2 或 3 整除了，因为能够被整除肯定就是 `getMin(n // 2) + 1` 或 `getMin(n // 3) + 1`
    而如果不能整除那么肯定需要多经历几次常规的 `+1` 操作，所以下面的解法中使用了 `min(getMin(n // 2) + n % 2 + 1, getMin(n // 3) + n % 3 + 1)`
    """
    def minDays(self, n: int) -> int:
        def getMin(n):
            if n == 0: return 0
            if n == 1: return 1
            if n in storeDays: return storeDays[n]
            target = min(
                getMin(n // 2) + n % 2 + 1,
                getMin(n // 3) + n % 3 + 1
            )
            storeDays[n] = target
            return target

        storeDays = {}
        return getMin(n)


if __name__ == "__main__":
    test = [
        10,  # 4
        6,  # 3
        1,  # 1
        56,  # 6
        9459568,  # 21
    ]
    start = time.perf_counter()
    for item in test:
        result = Solution3().minDays(item)
        print(f'{item} => {result}')
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
