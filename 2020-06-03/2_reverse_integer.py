"""
题目： 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
示例 1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


class Solution1:
    def reverse(self, x: int) -> int:
        xSymbol = 1 if x > 0 else -1
        xDiv = abs(x)
        xMod = 0
        y = 0
        while xDiv or xMod:
            y = y * 10 + xMod
            xDiv, xMod = divmod(xDiv, 10)
        y *= xSymbol
        if -2147483648 > y or y > 2147483647:
            return 0
        return y


class Solution2:
    def reverse(self, x: int) -> int:
        THRESHOLD = (1<<31) if x < 0 else (1<<31) -1
        xAbs = abs(x)
        y = 0
        while xAbs:
            xAbs, tmp = divmod(xAbs, 10)
            if y > THRESHOLD // 10 or (y == THRESHOLD // 10 and tmp >= THRESHOLD % 10):
                return 0
            y = y * 10 + tmp
        
        return y if x > 0 else -1 * y


if __name__ == '__main__':
    # x = 123
    # x = -123
    # x = 120
    x = 1534236469
    # x = 2147483647
    # [-2147483648, 2147483647]
    y = Solution2().reverse(x)
    print(f'{x} reverse is {y}')
