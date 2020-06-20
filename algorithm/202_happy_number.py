"""
题目：https://leetcode-cn.com/problems/happy-number/

编写一个算法来判断一个数 n 是不是快乐数。
「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。
如果 n 是快乐数就返回 True ；不是，则返回 False 。

示例：
输入：19
输出：true
解释：
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""

import time
from typing import List


class Solution1:
    """
    采用暴力法，利用hash表来存储已经平方和的中间结果，如果最新的数据在该hash表中，那么就退出计算
    最后判断结果是否为1
    """
    def isHappy(self, n: int) -> bool:
        tmpPowerNums = set()
        while n not in tmpPowerNums:
            tmpPowerNums.add(n)
            n = self.powerSum(n)
        return n == 1

    @classmethod
    def powerSum(cls, n):
        tmp = 0
        while n:
            n, nMod = divmod(n, 10)
            tmp += nMod ** 2
        return tmp
    
    @classmethod
    def powerSum2(cls, n):
        """
        通过遍历字符串每一位来计算每一位的平行和
        """
        return sum([int(i) ** 2 for i in repr(n)])


class Solution2:
    """
    根据官网的提示，采用 快慢指针法
    https://leetcode-cn.com/problems/happy-number/solution/kuai-le-shu-by-leetcode-solution/
    这里的快慢指针法，使用的是弗洛伊德环查找算法，用快慢的两个指针向前计算，快的每次计算两次，慢的每次计算一次
    最终慢指针的值会与快指针的值相等，就表示遇到了环，就退出
    最后判断相等的值是否为1
    """
    def isHappy(self, n: int) -> bool:
        slow = fast = n
        while True:
            slow = self.powerSum(slow)
            fast = self.powerSum(fast)
            fast = self.powerSum(fast)
            if slow == fast: break
        return slow == 1

    @classmethod
    def powerSum(cls, n):
        tmp = 0
        while n:
            n, nMod = divmod(n, 10)
            tmp += nMod ** 2
        return tmp


class Solution3:
    """
    根据官网的提示，采用数学法，如果不是快乐数的话，那么一定是在如下的循环体中循环
    https://leetcode-cn.com/problems/happy-number/solution/kuai-le-shu-by-leetcode-solution/
    4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4
    """
    def isHappy(self, n: int) -> int:
        stopNums = {1, 4, 16, 37, 58, 89, 145, 42, 20}
        while True:
            n = self.powerSum(n)
            if n in stopNums: break
        return n == 1

    @classmethod
    def powerSum(cls, n):
        tmp = 0
        while n:
            n, nMod = divmod(n, 10)
            tmp += nMod ** 2
        return tmp


if __name__ == "__main__":
    test = [
        19, # true
    ]
    start = time.perf_counter()
    for i in test:
        result = Solution3().isHappy(i)
        print(f'{i} is happy? {"yes" if result else "no"}')
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
