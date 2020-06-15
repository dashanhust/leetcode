"""
题目：https://leetcode-cn.com/problems/integer-to-roman/
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。
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
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

输入: 58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.

输入: 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.
"""

class Solution1:
    """
    通过题目的定义对规则进行梳理如下
    """
    def intToRoman(self, num: int ) -> str:
        res = ''
        if num < 1 or num > 3999:
            return res
        numTimes = -1
        while num:
            num, numMod = divmod(num, 10)
            numTimes += 1
            tmpNum = numMod * (10 ** numTimes)
            if tmpNum < 4:
                tmpStr = 'I' * numMod
            elif tmpNum == 4:
                tmpStr = 'IV'
            elif tmpNum < 9:
                tmpStr = 'V' + 'I' * (numMod - 5)
            elif tmpNum == 9:
                tmpStr = 'IX'
            elif tmpNum < 40:
                tmpStr = 'X' * numMod
            elif tmpNum == 40:
                tmpStr = 'XL'
            elif tmpNum < 90:
                tmpStr = 'L' + 'X' * (numMod - 5)
            elif tmpNum == 90:
                tmpStr = 'XC'
            elif tmpNum < 400:
                tmpStr = 'C' * numMod
            elif tmpNum == 400:
                tmpStr = 'CD'
            elif tmpNum < 900:
                tmpStr = 'D' + 'C' * (numMod - 5)
            elif tmpNum == 900:
                tmpStr = 'CM'
            else:
                tmpStr = 'M' * numMod
            res = tmpStr + res
        return res


class Solution2:
    """
    对Solution1的运算做一些简化，将判断规则通过字典的方式进行简化
    """
    def intToRoman(self, num: int ) -> str:
        res = ''
        if num < 1 or num > 3999:
            return res

        numTimes = -1
        romanDict = {
            1: ['I', 'V'],
            10: ['X', 'L'],
            100: ['C', 'D'],
            1000: ['M']
        }
        specialDict = {
            4: 'IV',
            9: 'IX',
            40: 'XL',
            90: 'XC',
            400: 'CD',
            900: 'CM'
        }
        while num:
            num, numMod = divmod(num, 10)
            numTimes += 1
            multiple = 10 ** numTimes
            tmpNum = numMod * multiple

            tmpStr = specialDict.get(tmpNum)
            if tmpStr:
                res = tmpStr + res
                continue

            if numMod < 4:
                tmpStr = romanDict[multiple][0] * numMod
            else:
                tmpStr = romanDict[multiple][1] + romanDict[multiple][0] * (numMod - 5)
            res = tmpStr + res
        return res


class Solution3:
    """
    贪婪算法：https://leetcode-cn.com/problems/integer-to-roman/solution/zheng-shu-zhuan-luo-ma-shu-zi-by-leetcode/
    由于古罗马表示的数字有限，所以可以将待转化的数字依次用最大的古罗马数字来进行转换
    """
    def __init__(self):
        self.digits = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
    
    def intToRoman(self, num: int) -> str:
        romonDigits = []
        for value, symbol in self.digits:
            count, num = divmod(num, value)
            if not count: continue
            romonDigits.append(symbol * count)
        return ''.join(romonDigits)


class Solution4:
    """
    硬编码方法，就是将所有可能的情况都给穷举出来
    https://leetcode-cn.com/problems/integer-to-roman/solution/zheng-shu-zhuan-luo-ma-shu-zi-by-leetcode/
    """
    def intToRoman(self, num: int) -> str:
        thousands = ['', 'M', 'MM', 'MMM']
        hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        return thousands[num // 1000] + \
               hundreds[num % 1000 // 100] + \
               tens[num % 100 // 10] + \
               ones[num % 10]


    
if __name__ == '__main__':
    test = [
        3, # 'III'
        4, # 'IV'
        9, # 'IX'
        58, # 'LVIII'
        1994, # 'MCMXCIV'
    ]
    for num in test:
        result = Solution4().intToRoman(num)
        print(f'{num} to roman {result}')



