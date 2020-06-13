"""
题目： 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
      请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
      你可以假设 nums1 和 nums2 不会同时为空。
环境：python3.6
样例：
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0

nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        allnums = nums1 + nums2
        allnums.sort()
        len_allnums = len(allnums)
        if len_allnums % 2:
            return allnums[len_allnums // 2] * 1.0
        else:
            return (allnums[len_allnums // 2 - 1] + allnums[len_allnums // 2]) / 2.0


if __name__ == '__main__':
    # nums1 = [1, 3]
    # nums2 = [2]
    nums1 = [1, 2]
    nums2 = [3, 4]
    result = Solution().findMedianSortedArrays(nums1, nums2)
    print(f'{result}')
