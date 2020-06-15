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
        采用动态规划的解法，先得找出状态转移方程
        dp(i, j) 表示s的前i个字符与p的前j个字符串匹配是否匹配完全，值为False/True
        那么需要从 dp(i-1, j-1) 和 s[i] 与 p[j] 来判断出 dp(i, j)
        当 p[j] in ('.', s[i]) 时， dp(i, j) = dp(i-1, j-1) 
        当 p[j] == '*' 时，
            如果 p[j] 重复前面的字符 p[j-1] 0 次时，dp(i, j) = dp(i, j-2)
            如果 p[j] 重复前面的字符 p[j-1] 1 次时，dp(i, j) = dp(i-1, j-1) and p[j-1] in ('.', s[i])
        否则，dp(i, j) = False
        """
        m = len(s)
        n = len(p)
        dp = dict()  # m * n 列矩阵，m表示字符串s的长度；n表示匹配串p的长度
        dp[0, 0] = True
        for i in range(1, m + 1): # 有s没有p的情况
            dp[i, 0] = False
        for j in range(1, n + 1): # 有p没有s的情况
            if j == 1 or p[j - 1] != '*':
                dp[0, j] = False
            else:
                dp[0, j] = dp[0, j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] in {'.', s[i - 1]}:
                    dp[i, j] = dp[i - 1, j - 1]
                elif j >= 2 and p[j - 1] == '*':
                    # 匹配0次
                    dp[i, j] = dp[i, j - 2]
                    if not dp[i, j] and (p[j - 2] in {'.', s[i - 1]}):  # 匹配1次或者多次
                        dp[i, j] = dp[i, j - 1] or dp[i - 1, j]
                else:
                    dp[i, j] = False
        return dp[m, n]


if __name__ == '__main__':
    test = [
        # ('aa', 'a'), # false
        # ('aa', 'a*'), # true
        # ('ab', '.*'), # ture
        ('aab', 'c*a*b'), # true
        # ('mississippi', 'mis*is*p*.'), # false
        # ('aasdfasdfasdfasdfas', 'aasdf.*asdf.*asdf.*asdf.*s') # true
        # ('fa', 'f.*a') # true
    ]
    for s, p in test:
        result = Solution3().isMatch(s, p)
        print(f's:{s} p:{p} isMatch ? {result} ')