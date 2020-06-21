"""
题目：https://leetcode-cn.com/problems/factorial-trailing-zeroes/

给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。

示例 2:
输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为 O(log n) 
"""

import time
from typing import List
import math


class Solution1:
    """
    暴力解法：
    先求解出n的阶乘，然后与10取余的结果如果为0，说明最后一位是0，一直到取余不为0为止
    """
    def trailingZeroes(self, n: int) -> int:
        output = 0
        nFactorial = math.factorial(n)
        nFactorial, nMod = divmod(nFactorial, 10)
        while 0 < nFactorial and nMod == 0:
            output += 1
            nFactorial, nMod = divmod(nFactorial, 10)
        return output


class Solution2:
    """
    数论法：
    有多少个0，可以表示为 n! = a * 10^k = a * 5^k * 2^k 其中a表示末尾没有0的整数
    所以问题就变成了求解 1, 2, 3, ... n-1, n 里面关于5的倍数中，关于5的倍数的数量
    例如 n = 21 关于5的倍数有 5 10 15 20 由于有
    5 = 1 * 5^1
    10 = 2 * 5^1
    15 = 3 * 5^1
    20 = 4 * 5^1
    所以 21! 的结尾中有 1 + 1 + 1 + 1 = 4 个0
    """
    def trailingZeroes(self, n: int) -> int:
        output = 0
        fileMultiple = 5
        for fileMultiple in range(5, n + 1, 5):
            five_power = 5
            while fileMultiple % five_power == 0:
                output += 1
                five_power *= 5
        return output


class Solution3:
    """
    那么如何高效的计算方法2中的计算因子5呢，
    5, 10, 15, ... m-5, m, n  其中m是离n最近的可以被5整除的数 =》
    1*5， 2*5， 3*5， ... k1*5, n 其中 m=k1*5
    而有一些数还能继续被5整除，例如25，50 ... 所以可以继续整理数据为
    25, 50, 75, ... k2*25, n 其中 k2*25 表示离n最近的可以被25整除的数
    继续还有能被125整除的，能被625整除的...

    所以总结如下：
    所有需要整除的次数 = 能被5整除最大k1 + 能被25整除的最大k2 + ...
    """
    def trailingZeroes(self, n: int) -> int:
        output = 0
        fileMultiple = 5
        while n // fileMultiple:
            output += (n // fileMultiple)
            fileMultiple *= 5
        return output


class Solution4:
    """
    根据方法3中的规则，我们可以将其转化为递归的方式来解决
    """
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            return n // 5 + self.trailingZeroes(n // 5)


if __name__ == "__main__":
    test = [
        3, # 0
        5, # 1
        30, # 7
        40, # 9
        8527
    ]
    start = time.perf_counter()
    for n in test:
        result = Solution4().trailingZeroes(n)
        print(f'{n} factorial zeroes is {result}')
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
