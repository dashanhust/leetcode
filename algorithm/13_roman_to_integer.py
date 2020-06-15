"""
题目：https://leetcode-cn.com/problems/roman-to-integer/
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

示例 1:
输入: "III"
输出: 3

示例 2:
输入: "IV"
输出: 4

示例 3:
输入: "IX"
输出: 9

示例 4:
输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.

示例 5:
输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
"""


class Solution1:
    """
    通过阅读题目，得知所有罗马数字的情况，大的罗马数字在前面，小的罗马数字在后面，并且记录了特殊情况(self._specials)
    """
    def __init__(self):
        self._digits = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        self._specials = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
    def romanToInt(self, s: str) -> int:
        sLen = len(s)
        if not sLen: return 0
        res = self._digits[s[0]]
        for i in range(1, sLen):
            if s[i - 1: i + 1] in self._specials.keys():
                res = res - self._digits[s[i - 1]] + self._specials[s[i - 1: i + 1]]
            elif self._digits[s[i]] > self._digits[s[i - 1]]:
                res -= self._digits[s[i]]
            else:
                res += self._digits[s[i]]
        return res


class Solution2:
    """
    数字规律参考如下地址：
    https://leetcode-cn.com/problems/roman-to-integer/solution/yong-shi-9993nei-cun-9873jian-dan-jie-fa-by-donesp/
    一般情况下如果第i个罗马字符 s[i] > s[i+1] 那么第i个罗马字符的数字做加法，否则第i个罗马字符的数字做减法
    并且最后一个罗马字符肯定是做加法，因为该罗马字符后面没有其他字符进行判断了
    """
    def __init__(self):
        self._digits = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    def romanToInt(self, s: str) -> int:
        res = 0
        sLen = len(s)
        if not sLen: return res
        preNum = self._digits[s[0]]
        for i in range(1, sLen):
            num = self._digits[s[i]]
            if preNum < num:
                res -= preNum
            else:
                res += preNum
            preNum = num
        res += preNum
        return res


if __name__ == '__main__':
    test = [
        'III',  # 3
        'IV',  # 4
        'IX',  # 9
        'LVIII',  # 58
        'MCMXCIV'  # 1994
    ]
    for s in test:
        result = Solution2().romanToInt(s)
        print(f'{s} romanToInt {result}')
