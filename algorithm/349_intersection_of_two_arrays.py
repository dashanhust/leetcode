"""
题目：https://leetcode-cn.com/problems/intersection-of-two-arrays/

给定两个数组，编写一个函数来计算它们的交集。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]

示例 2：
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
 
说明：
输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。
"""

import time
from typing import List


class Solution1:
    """
    使用集合set，在判断in/container的情况，时间复杂度为 O(1)
    python中一些常见数据结构例如 list / dict / set 的常见操作的时间复杂度如下
    https://www.cnblogs.com/harvey888/p/6659061.html
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 使nums1是小数组，nums2是大数组
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        ans = []
        smallSet = set(nums1)
        bigSet = set(nums2)

        ans = [item for item in smallSet if item in bigSet]
        return ans


if __name__ == "__main__":
    test = [
        [[1,2,2,1], [2,2]], # [2]
        [[4,9,5], [9,4,9,8,4]], # [9, 4]
    ]
    start = time.perf_counter()
    for (nums1, nums2) in test:
        result = Solution1().intersection(nums1, nums2)
        print(f'result: {result}')
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
