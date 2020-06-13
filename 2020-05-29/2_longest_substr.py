"""
题目：给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
环境：python3.6
案例：
    输入: "abcabcbb"
    输出: 3 
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_str = len(s)
        if len_str == 0:
            return 0
        start_idx = 0
        end_idx = 1
        len_max_sub = 0
        while end_idx < len_str:
            i_str = s[end_idx]
            sub_str = s[start_idx:end_idx]
            if i_str in sub_str:
                len_max_sub = max(len_max_sub, end_idx - start_idx)
                start_idx = start_idx + sub_str.find(i_str) + 1
            end_idx += 1
        len_max_sub = max(len_max_sub, end_idx - start_idx)
        return len_max_sub

if __name__ == '__main__':
    # s = 'abcabcbb'
    # s = 'bbbbb'
    s = 'pwwkew'
    result = Solution().lengthOfLongestSubstring(s)
    print(f'{s} max substring length: {result}')

