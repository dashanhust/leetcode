"""
题目：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""

import time
from typing import List
from collections import defaultdict


class Solution1:
    """
    滑动窗口法, 左闭右开区间，所以我们可以让right从0开始一直到数组的长度
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)
        left = right = distance = 0
        lenS = len(s)

        while right < lenS:
            # 右边元素移入窗口
            c = s[right]
            right += 1
            # 处理窗口内容
            window[c] += 1

            # 判断是否要收敛窗口
            while window[c] > 1:
                # 左侧元素移出窗口
                d = s[left]
                left += 1
                # 处理窗口内容
                window[d] -= 1
            distance = max(distance, right - left)
        return distance


class Solution2:
    """
    滑动窗口与散列表的组合
    参考： https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetc-2/
    模式识别1： 一旦涉及出现次数，就需要使用散列表
    模式识别2： 涉及子串，考虑滑动窗口
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        lenS = len(s)
        left = right = distance = 0
        window = {}

        while right < lenS:
            c = s[right]
            if window.get(c, -1) > -1:
                distance = max(distance, right - left)
                # print(f'left: {left}; right: {right}; window: {window}')
                startIndex = window[c] + 1
                while left < startIndex:
                    del window[s[left]]
                    left += 1
            window[c] = right
            right += 1
        return max(distance, right - left)


class Solution3:
    """
    这里列出一位网友给出的python窗口比较优秀的解法
    上面的解法中都要用到delete窗口中已经存在的字符，这里我们可以这样想:
    
    如果元素在窗口字典中的下表 小于 窗口的起始位置的话，说明窗口已经滑动过了这个元素，我们是可以不用理会的
    注意窗口是 左闭右开 [left, right)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, distance = 0, 0
        window = {}

        for right, item in enumerate(s):
            if item in window and window[item] >= left:
                left = window[item] + 1
                window[item] = right
            else:
                window[item] = right
                distance = max(distance, right - left + 1)

        return distance


if __name__ == "__main__":
    test = [
        "abcabcbb", # 3
        "bbbbb", # 1
        "pwwkew", # 3
        " ", # 1
        "aab", # 2
    ]
    start = time.perf_counter()
    for s in test:
        result = Solution1().lengthOfLongestSubstring(s)
        print(f'{s} lengthOfLongestSubstring => {result}')
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
