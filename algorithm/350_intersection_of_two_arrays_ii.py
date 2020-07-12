"""
题目：https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/

给定两个数组，编写一个函数来计算它们的交集。

示例 1:
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]

示例 2:
输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]

说明：
输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。

进阶:
如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
"""

import time
from typing import List
from collections import defaultdict


class Solution1:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 使nums1是小数组，nums2是大数组
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        # 定义一个hash表，里面存储的是小数组的hash值
        smallDict = defaultdict(int)
        smallLen = len(nums1)
        for item in nums1:
            smallDict[item] += 1

        # 遍历大数组，获取交集元素
        ans = []
        for item in nums2:
            if smallLen == 0: break
            if smallDict[item] > 0:
                smallDict[item] -= 1
                smallLen -= 1
                ans.append(item)
        return ans


if __name__ == "__main__":
    test = [
        [[1,2,2,1], [2,2]], # [2,2]
        [[4,9,5], [9,4,9,8,4]], # [4,9]
    ]
    start = time.perf_counter()
    for (nums1, nums2) in test:
        result = Solution1().intersect(nums1, nums2)
        print(f'result: {result}')
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
