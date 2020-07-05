"""
题目：https://leetcode-cn.com/problems/permutation-in-string/

给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").

示例2:
输入: s1= "ab" s2 = "eidboaoo"
输出: False

注意：
输入的字符串只包含小写字母
两个字符串的长度都在 [1, 10,000] 之间
"""

import time
from typing import List
from collections import Counter, defaultdict


class Solution1:
    """
    滑动窗口法
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        target = defaultdict(int)
        left = right = distance = 0
        lenS2 = len(s2)
        start, length = 0, lenS2 + 1
        ans = False

        while right < lenS2:
            # 右元素移动
            c = s2[right]
            right += 1
            # 修改窗口内容
            target[c] += 1
            if need[c] == target[c]:
                distance += 1

            # print(f'left: {left}; right: {right}; distance: {distance}')

            # 缩减窗口
            while distance == len(need):
                # 左元素移动
                d = s2[left]
                left += 1
                target[d] -= 1
                # 修改窗口内容
                if need[d] > target[d]:
                    distance -= 1
                    if right - left + 1 < length:
                        start = left - 1
                        length = right - left +1
                        if length == len(s1):
                            ans = True
        # return [s2[start:start + length], ans, start, length]
        return ans


if __name__ == "__main__":
    test = [
        ["ab", "eidbaooo"], # True
        ["ab", "eidboaoo"], # False
    ]
    start = time.perf_counter()
    for (s1, s2) in test:
        result = Solution1().checkInclusion(s1, s2)
        print(f'{s2} check inclusion {s1} => {result}')
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
