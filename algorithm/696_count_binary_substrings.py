"""
题目：给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。

重复出现的子串要计算它们出现的次数。

示例 1 :
输入: "00110011"
输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

请注意，一些重复出现的子串要计算它们出现的次数。

另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。

示例 2 :
输入: "10101"
输出: 4
解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。

注意：
s.length 在1到50,000之间。
s 只包含“0”或“1”字符。
"""

import time
from typing import List


class Solution1:
    """
    思路：给定起始数据，从左往右数和左侧不同的数据，最远距离就是此时左侧
    """
    def countBinarySubstrings(self, s: str) -> int:
        lenS, cnt, i = len(s), 0, 0
        while i < lenS - 1:
            invert = '1' if s[i] == '0' else '0'
            has_invert = False
            for j in range(i + 1, lenS):
                if s[j] == invert:
                    has_invert = True
                    break
            if not has_invert: break

            for k in range(j, min(j + j -i, lenS)):
                if s[k] != invert: 
                    k -= 1
                    break
            cnt += (k - j + 1)
            # print(f'"{s}" i:{i}; j:{j}; k:{k} => cnt:{cnt}')
            i = j
        return cnt


class Solution2:
    """
    思路：按字符分组，例如 "00111011" 将0和1连续出现的次数分别标记为 [2, 3, 1, 2]，由于题目要求是连续的0和连续的1组成的子字符串。
    所以经过次数统计后的数组，相邻的元素，选择数据小的数据，就是可以出现的对称字符串数量。
    所以上面例子的结果为 min(2, 3) + min(3, 1) + min(1, 2) = 2 + 1 + 1 = 4
    """
    def countBinarySubstrings(self, s: str) -> int:
        lenS, strCntList = len(s), []
        left = 0
        for i in range(1, lenS):
            if s[left] != s[i]:
                strCntList.append(i - left)
                left = i
        strCntList.append(lenS - left)
        cnt = 0
        for i in range(1, len(strCntList)):
            cnt += min(strCntList[i-1], strCntList[i])
        return cnt


class Solution3:
    """
    思路：方法2中使用了字符分组的方法，但是增加了一个数组，这里我们可以使用双指针的方法，使用一个中间变量这样可以避免用一个中间数组来存储字符分组个数的情况
    """
    def countBinarySubstrings(self, s: str) -> int:
        lenS, cnt, preCnt, pre = len(s), 0, 0, 0
        for cur in range(1, lenS):
            if s[cur] != s[pre]:
                cnt += min(preCnt, cur - pre)
                preCnt = cur - pre
                pre = cur
        cnt += min(preCnt, lenS - pre)
        return cnt


if __name__ == "__main__":
    test = [
        ['00110011', 6],
        ['10101', 4],
        ['00100', 2],
        ['00111011', 4]
    ]
    start = time.perf_counter()
    for s, n in test:
        result = Solution3().countBinarySubstrings(s)
        print(f'{s} => {result} {"==" if result == n else "!="} {n}')
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
