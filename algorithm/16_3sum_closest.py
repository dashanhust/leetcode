"""
题目： https://leetcode-cn.com/problems/3sum-closest/

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

示例：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 
提示：
3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
"""

from typing import List


class Solution1:
    """
    采用排序和双指针法
    当然其中有一些优化的地方：
    1. 变量赋值，采取列表表达式的方式赋值， 例如： start, end = i + 1, numsLen - 1
    2. 尽量缩短比较范围
        当 nums[i] + nums[start] + nums[start + 1] >= target 时，用 nums[start + 2:] 数据相加，肯定更加大，就不用再选取了
        当 nums[i] + nums[end - 1] + nums[end] <= target 时，用 nums[start:end - 2] 数据相加，肯定更小，就不用再选取了
    """
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        numsLen = len(nums)
        for i in range(numsLen-2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            start, end = i + 1, numsLen - 1
            if nums[i] + nums[start] + nums[start + 1] >= target:
                end = start + 1
            if nums[i] + nums[end - 1] + nums[end] <= target:
                start = end - 1
            while start < end:
                tmpSum = nums[i] + nums[start] + nums[end]
                if tmpSum == target:
                    return target
                elif tmpSum < target:
                    start += 1
                else:
                    end -= 1
                if abs(target - tmpSum) < abs(target - res):
                    res = tmpSum
        return res


if __name__ == '__main__':
    test = [
        ([-1,2,1,-4], 1),
        ([0,1,2], 3)
    ]
    for nums, target in test:
        result = Solution1().threeSumClosest(nums, target)
        print(f'{nums} -> {target} : {result}')
