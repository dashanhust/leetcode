"""
题目：https://leetcode-cn.com/problems/longest-repeating-character-replacement/

给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。

注意:
字符串长度 和 k 不会超过 104。

示例 1:
输入:
s = "ABAB", k = 2
输出:
4

解释:
用两个'A'替换为两个'B',反之亦然。

示例 2:
输入:
s = "AABABBA", k = 1
输出:
4

解释:
将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
子串 "BBBB" 有最长重复字母, 答案为 4。
"""

import time
from typing import List
from collections import defaultdict


class Solution1:
    """
    滑动窗口
    参考：https://leetcode-cn.com/problems/longest-repeating-character-replacement/solution/tong-guo-ci-ti-liao-jie-yi-xia-shi-yao-shi-hua-don/
    定义一个窗口 [left, right] 满足条件: right - left + 1 <= 里面的元素出现次数最多的字母的次数 + k
    如果后面的元素加进来后不满足，那么 left++ 且 right++ 为什么两个都加1呢，因为这个窗口的长度是我们历史上知道的满足条件的最大宽度窗口
    这样窗口一直向右移动，一直到right到达了最后一个元素，此时窗口的长度就是答案
    """
    def characterReplacement(self, s: str, k: int) -> int:
        windowDict = defaultdict(int)
        left, right, lenS = 0, 0, len(s)

        while right < lenS:
            windowDict[s[right]] += 1
            if right - left + 1 > max(windowDict.values()) + k:
                windowDict[s[left]] -= 1
                left += 1
                right += 1
            else:
                right += 1

        return right - left


if __name__ == "__main__":
    test = [
        ["ABAB", 2], # 4
        ["AABABBA", 1], # 4
        ["ABBB", 2], # 4
    ]
    start = time.perf_counter()
    for (s, k) in test:
        result = Solution1().characterReplacement(s, k)
        print(f"s: {s}; k: {k}; result: {result}")
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
