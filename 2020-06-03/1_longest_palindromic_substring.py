"""
题目：给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。回文指的是正着读和反着读一样
环境：python3.6
样例：
    示例 1：
    输入: "babad"
    输出: "bab"
    注意: "aba" 也是一个有效答案。

    示例 2：
    输入: "cbbd"
    输出: "bb"
"""


class Solution1:
    """
    暴力解法 两边向中间扩散
    时间复杂度： O(n**3)
    空间复杂度： O(1)
    """
    def longestPalindrome(self, s: str) -> str:
        sLen = len(s)
        maxLen = 1
        begin = 0
    
        # 枚举所有长度严格大于1的子串
        for i in range(sLen):
            for j in range(i+1, sLen):
                isValidPalindromic = self.validPalindromic(s, i , j)
                isLarge = j - i + 1 > maxLen
                if isValidPalindromic and isLarge:
                    maxLen = j - i + 1
                    begin = i
        return s[begin:begin + maxLen]

    @staticmethod
    def validPalindromic(s: str, i: int, j: int) -> bool:
        """ 判断子串是否是回文串 """
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                break
        else:
            return True
        return False


class Solution2:
    """
    中心扩散法  -> 中间向两边扩散
    需要考虑奇数长度回文字符串、偶数长度回文字符串
    时间复杂度: O(n**2)
    空间复杂度: O(1)
    """
    def longestPalindrome(self, s: str) -> str:
        sLen = len(s)
        maxLen = 1
        begin = 0
        
        for i in range(sLen - 1):
            # 第一个元素没有左边元素，最后一个元素没有右边元素，所以可以不用处理
            oddLen = self.expandAroundCenter(s, i, i)
            evenLen = self.expandAroundCenter(s, i, i + 1)
            if max(oddLen, evenLen) > maxLen:
                maxLen = max(oddLen, evenLen)
                begin = i - (maxLen - 1) // 2
        return s[begin:begin + maxLen]
    
    @staticmethod
    def expandAroundCenter(s: str, i: int, j: int) -> int:
        """ 返回字符从下标 i,j 往两边扩散的最长回文子串长度 """
        sLen = len(s)
        while i >= 0 and j < sLen:
            if s[i] == s[j]:
                i -= 1
                j += 1
            else:
                break
        return j - i - 1


class Solution3:
    """
    动态规划 -> 空间换时间
    状态转移方程： P(i, j) = s[i] == s[j] or (j - i < 3 or P(i+1, j-1))
    其中 j - i < 3 表示s[i:j+1]的长度为2、3时，只需要比较s[i]是否等于s[j]即可，而i==j的情况，就肯定为True了
    P(i, j) 表示字符串 s[i:j+1] 是否是回文字符串，值为 False / True
    表示判断的子串的长度如果不大于3的话，就没有校验这个子串的必要了
    在状态转移方程中，我们是从长度较短的字符串向长度较长的字符串进行转移
    """
    def longestPalindrome(self, s: str) -> str:
        sLen = len(s)
        dp = [[False] * sLen for _ in range(sLen)]
        maxLen = 1
        begin = 0
        
        for j in range(1, sLen):
            for i in range(j):
                if j - i < 3:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                # 记录最长的回文子串
                if dp[i][j] and j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    begin = i
        return s[begin:begin + maxLen]


if __name__ == '__main__':
    # s = 'babad'
    # s = 'cbbd'
    s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    # result = Solution1().longestPalindrome(s)
    result = Solution1().longestPalindrome(s)
    print(f'{s} longest palindrom is {result}')