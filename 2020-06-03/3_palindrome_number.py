"""
题目：判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
环境: python3.6
示例 1:
输入: 121
输出: true

示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

进阶:
你能不将整数转为字符串来解决这个问题吗？
"""


class Solution1:
    """ 使用字符串 """
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        xStr = str(x)
        xLen = len(xStr)
        beginIdx = 0
        endIdx = xLen - 1
        while beginIdx <= endIdx and xStr[beginIdx] == xStr[endIdx]:
            beginIdx += 1
            endIdx -= 1
        if beginIdx > endIdx:
            return True
        else:
            return False


class Solution2:
    """ 不使用字符串 """
    def isPalindrome(self, x: int) -> bool:
        # 负数、最后一位为0的正数都不是回文整数
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        xReverse = 0
        xMod = 0
        while x > xReverse:
            x, xMod = divmod(x, 10)
            xReverse = 10 * xReverse + xMod
        return x == xReverse or 10 * x + xMod == xReverse

if __name__ == '__main__':
    # x = 121
    # x = -121
    x = 10
    result = Solution2().isPalindrome(x)
    print(f'{x} is palindrome. {result}')