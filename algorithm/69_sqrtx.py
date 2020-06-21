"""
题目：https://leetcode-cn.com/problems/sqrtx/

实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。
"""

import time
from typing import List
import math


class Solution1:
    """
    二分查找法
    """
    def mySqrt(self, x: int) -> int:
        left, ans, right = 0, -1, x

        while left <= right:
            middle = (left + right) // 2
            tmpPower = middle ** 2
            if tmpPower < x:
                ans = middle
                left = middle + 1
            elif tmpPower > x:
                right = middle - 1
            else:
                return middle
        return ans


class Solution2:
    """
    袖珍查找法
    sqrt(x) = sqrt(e^(log(x))) = e^(log(x)/2)
    """
    def mySqrt(self, x: int) -> int:
        if x < 1: return x
        res = int(math.exp(math.log(x) / 2))
        return res + 1 if (res + 1) ** 2 <= x else res


class Solution3:
    """
    牛顿法：https://leetcode-cn.com/problems/sqrtx/solution/er-fen-cha-zhao-niu-dun-fa-python-dai-ma-by-liweiw/
    """
    def mySqrt(self, x: int) -> int:
        curl = 1
        while True:
            pre = curl
            curl = (pre + x / pre) / 2
            if abs(pre - curl) < 1e-6:
                return int(pre)


if __name__ == "__main__":
    test = [
        0, # 0
        4, # 2
        8, # 2
        9, # 3
        10, # 3
    ]
    start = time.perf_counter()
    for i in test:
        result = Solution3().mySqrt(i)
        print(f'{i} sqrt => {result}')
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
