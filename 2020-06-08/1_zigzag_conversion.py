"""
题目：将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
L   C   I   R
E T O E S I I G
E   D   H   N

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:
输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"

示例 2:
输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"

解释:
L     D     R
E   O E   I I
E C   I H   N
T     S     G
"""

import math


class Solution1:
    def convert(self, s: str, numRows: int) -> str:
        sLen = len(s)
        if numRows <= 1 or sLen <= numRows:
            return s
        if numRows == 2:
            return s[0::2] + s[1::2]
        sDiv, sMod = divmod(sLen, numRows + max(numRows - 2, 0)) 
        numColum = sDiv * 2 + math.ceil(sMod / numRows)
        sMatrix = [[''] * numRows for _ in range(numColum)]
        begin = 0
        for i in range(numColum):
            if i % 2 == 0:
                for j, value in enumerate(s[begin:begin + numRows]):
                    sMatrix[i][j] = s[begin + j]
                begin += numRows
            else:
                for j, value in enumerate(s[begin:begin + numRows - 2]):
                    sMatrix[i][numRows - j - 2] = s[begin + j]
                begin += max(numRows - 2, 0)

        result = []
        for i in range(numRows):
            iRow = [row[i] for row in sMatrix]
            result.append(''.join(iRow))
        return ''.join(result)


class Solution2:
    def convert(self, s: str, numRows: int) -> str:
        sLen = len(s)
        if numRows <= 1 or sLen <= numRows:
            return s
        if numRows == 2:
            return s[0::2] + s[1::2]
        sDiv, sMod = divmod(sLen, numRows + max(numRows - 2, 0)) 
        numColum = sDiv * 2 + math.ceil(sMod / numRows)
        sMatrix = [[''] * numColum for _ in range(numRows)]
        begin = 0
        for i in range(numColum):
            if i % 2 == 0:
                for j, value in enumerate(s[begin:begin + numRows]):
                    sMatrix[j][i] = s[begin + j]
                begin += numRows
            else:
                for j, value in enumerate(s[begin:begin + numRows - 2]):
                    sMatrix[numRows - j - 2][i] = s[begin + j]
                begin += max(numRows - 2, 0)

        result = []
        for i in sMatrix:
            result.append(''.join(i))
        return ''.join(result)


class Solution3:
    def convert(self, s: str, numRows: int) -> str:
        """
        这里列出官方的算法，通过当前行和移动方向来控制字符的移动
        https://leetcode-cn.com/problems/zigzag-conversion/submissions/
        """
        if numRows <= 1 or numRows >= len(s):
            return s
        curRow = 0
        goingDown = False
        sMatrix = [''] * numRows
        for i in s:
            sMatrix[curRow] += i
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1
        return ''.join(sMatrix)



if __name__ == '__main__':
    s = 'LEETCODEISHIRING'
    numRows = 3
    result = Solution3().convert(s, numRows)
    print(f'{s} convert to {result}')
