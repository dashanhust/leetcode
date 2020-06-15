"""
题目：https://leetcode-cn.com/problems/longest-common-prefix/

编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明: 所有输入只包含小写字母 a-z 。
"""

from typing import List


class Solution1:
    """
    纵向扫描法
    比较每个字符串的同一个位置的字符串是否相等
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        minStrLen = min([len(item) for item in strs])
        longestLen = minStrLen
        for i in range(minStrLen):
            itemSet = set([item[i] for item in strs])
            if len(itemSet) != 1:
                longestLen = i
                break
        return strs[0][:longestLen]


class Solution2:
    """
    横向扫描
    https://leetcode-cn.com/problems/longest-common-prefix/solution/zui-chang-gong-gong-qian-zhui-by-leetcode-solution/
    用LCP(S1 ... Sn) 表示字符串S1 ... Sn的最长公共前缀，可以得到如下表达式
    LCP(S1 ... Sn) = LCP(LCP(LCP(LCP(S1, S2), S3), ... Sn-1), Sn)
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strsNum = len(strs)
        if not strsNum: return ''
        res = strs[0]
        for i in range(1, strsNum):
            res = self.lcp(res, strs[i])
            if not res:
                break
        return res

    def lcp(self, str1: str, str2: str) -> str:
        minLen = min(len(str1), len(str2))
        for i in range(minLen):
            if str1[i] != str2[i]:
                return str1[:i]
        return str1[:minLen]


class Solution3:
    """
    分治法
    https://leetcode-cn.com/problems/longest-common-prefix/solution/zui-chang-gong-gong-qian-zhui-by-leetcode-solution/
    将数组中的字符串分成两组，分别得到两组中的最长公共前缀，然后计算出这两个前缀的最长公共前缀
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        strsNum = len(strs)
        return self.lcp(strs, 0, strsNum - 1)
    
    def lcp(self, strs: List[str], left: int, right: int) -> str:
        if left == right: return strs[left]
        mid = (left + right) // 2
        leftPrefix = self.lcp(strs, left, mid)
        rightPrefix = self.lcp(strs, mid + 1, right)
        return self.commonPrefix(leftPrefix, rightPrefix)

    def commonPrefix(self, str1: str, str2: str) -> str:
        minLen = min(len(str1),len(str2))
        idx = 0
        while (idx < minLen) and (str1[idx] == str2[idx]):
            idx += 1
        return str1[:idx]


class Solution4:
    """
    采用pythonzip的特性，空间换区时间的方法
    例如 strs = ['name', 'age', 'class']
    set(*strs) =>
    [
        ('n', 'a', 'c'),
        ('a', 'g', 'l'),
        ('m', 'e', 'a')
    ]
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for i in zip(*strs):
            if len(set(i)) == 1:
                res += i[0]
            else:
                break
        return res


class Solution5:
    """
    先对字符串列表进行排序，然后获取字符串最大值与最小值的最长公共前缀就可得到字符串列表的最长公共前缀
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        minStr = min(strs)
        maxStr = max(strs)
        idx = 0
        while (idx < len(minStr)) and (minStr[idx] == maxStr[idx]):
            idx += 1
        return minStr[:idx]


if __name__ == '__main__':
    test = [
        ["flower","flow","flight"],
        ["dog","racecar","car"]
    ]
    for strs in test:
        result = Solution5().longestCommonPrefix(strs)
        print(f'{strs} longestCommonPrefix {result}')