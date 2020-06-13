"""
题目：给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。

示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:
输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3:
输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

示例 4:
输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5:
输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
"""

import re


class Solution1:
    def isMatch(self, s: str, p: str) -> bool:
        match = re.match(p, s)
        return match.group() == s if match else False


class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        """
        参考： https://leetcode-cn.com/problems/regular-expression-matching/solution/ji-yu-guan-fang-ti-jie-gen-xiang-xi-de-jiang-jie-b/
        如果发现p中有 * ；那么该 * 与前面的字符要么匹配0次，要么匹配多次
        因为采用递归的方式，所以我们这里每次递归的时候，就假设要么匹配0次，要么匹配1次
        1. 匹配0次就是 self.isMatch(s[1:], p[1:])
        2. 匹配1次就是 self.isMatch(s[2:], p) 将匹配串向后移动2位
        """
        if not p:
            return not s
        
        firstMath = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or \
                    (firstMath and self.isMatch(s[1:], p))
        else:
            return firstMath and self.isMatch(s[1:], p[1:])


class Solution3:
    def isMatch(self, s: str, p: str) -> bool:
        """
        采用重叠子问题的解法来解决
        """
        memo = dict()  # 备忘录
        def dp(i, j):
            if (i, j) in memo: return memo[(i, j)]
            if j == len(p): return i == len(s)
            




if __name__ == '__main__':
    test = [
        ('aa', 'a'), # false
        ('aa', 'a*'), # true
        ('ab', '.*'), # ture
        ('aab', 'c*a*b'), # true
        ('mississippi', 'mis*is*p*.') # false
    ]
    for s, p in test:
        result = Solution2().isMatch(s, p)
        print(f's:{s} p:{p} isMatch ? {result} ')