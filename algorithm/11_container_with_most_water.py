"""
题目：https://leetcode-cn.com/problems/container-with-most-water/
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。
图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例：
输入：[1,8,6,2,5,4,8,3,7]
输出：49
"""

import time
from typing import List

class Solution1:
    """
    暴力解法
    """
    def maxArea(self, height: List[int]) -> int:
        lenHeight = len(height)
        area = 0
        if lenHeight < 2:
            return area
        
        for i in range(lenHeight - 1):
            for j in range(i + 1, lenHeight):
                ijMaxHeight = min(height[i], height[j])
                ijLen = j - i
                iArea = ijMaxHeight * ijLen
                area = max(area, iArea)
        return area


class Solution2:
    """
    双指针法，这里参考了这个链接的解法思路编写如下的代码
    https://leetcode-cn.com/problems/container-with-most-water/solution/container-with-most-water-shuang-zhi-zhen-fa-yi-do/
    思路：
    从列表两边开始往中间缩短，假设长度为n，那么最多有 C(n,2) 种状态的值，而每次就是要从缩减两边中较小的一边的索引开始
    因为如果从较大的一边开始缩减的话，得到的面积肯定是越来越小，毕竟水槽的宽度在减少，而高度也依然在减少的情况，肯定是面积越来越小的
    """
    def maxArea(self, height: List[int]) -> int:
        area = 0
        i = 0
        j = len(height) - 1
        while i < j:
            minHeight = min(height[i], height[j])
            area = max(area, minHeight * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return area


if __name__ == '__main__':
    test = [
        [1,8,6,2,5,4,8,3,7]
    ]
    start = time.clock()
    for height in test:
        result = Solution2().maxArea(height)
        print(f'maxArea is {result}')
    end = time.clock()
    print(f'{end} - {start} = {end - start}')
