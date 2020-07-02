"""
题目：https://leetcode-cn.com/problems/minimum-window-substring/

给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。
"""

import time
from typing import List


class Solution1:
    def minWindow(self, s: str, t: str) -> str:
      pass


if __name__ == "__main__":
    test = [
        ["ADOBECODEBANC", "ABC"]
    ]
    start = time.perf_counter()
    for (S, T) in test:
        result = Solution1().minWindow(S, T)
        print(f'{S} {T} minWindow => {result}')
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
