"""
题目：https://leetcode-cn.com/problems/grumpy-bookstore-owner/

今天，书店老板有一家店打算试营业 customers.length 分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。
在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。
书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。
请你返回这一天营业下来，最多有多少客户能够感到满意的数量。
 

示例：
输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
输出：16
解释：
书店老板在最后 3 分钟保持冷静。
感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
 

提示：
1 <= X <= customers.length == grumpy.length <= 20000
0 <= customers[i] <= 1000
0 <= grumpy[i] <= 1
"""

import time
from typing import List


class Solution1:
    """
    分析题目：
    求解customers和grumpy两个长度相同的列表中，grumpy值为1的同样位置的customer的值的和；
    还有customer里面长度为X的连续子数组中，没有进行上面计算的数据的和的最大值。

    我们用两个数组来表示
    """
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        # ans表示不使用技能的满意人的数量
        # grumpyAdd表示使用技能的满意人的数量
        # windowAdd表示长度为X的滑动窗口内，使用技能的满意人的数量
        # 通过遍历数组，计算滑动窗口中，满意人的数量的最大值，赋值给grumpyAdd
        # 最后的结果就是 ans + grumpyAdd
        ans, grumpyAdd, windowAdd = 0, 0, 0
        lenCustomers = len(customers)

        for i in range(lenCustomers):
            if i >= X and grumpy[i - X] == 1:
                windowAdd -= customers[i - X]
            if grumpy[i] == 0:
                ans += customers[i]
            else:
                windowAdd += customers[i]
                grumpyAdd = max(grumpyAdd, windowAdd)
        ans += grumpyAdd
        return ans


if __name__ == "__main__":
    test = [
        [[1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3], # 16
        [[4,10,10], [1,1,0], 2], # 24
    ]
    start = time.perf_counter()
    for (customers, grumpy, X) in test:
        result = Solution1().maxSatisfied(customers, grumpy, X)
        print(f'reuslt: {result}')
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
