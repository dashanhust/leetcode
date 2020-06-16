"""
题目： https://leetcode-cn.com/problems/4sum/

给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
注意：答案中不可以包含重复的四元组。

示例：
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

from typing import List


class Solution1:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        numsLen = len(nums)
        for i in range(numsLen - 3):
            if nums[i] * 4 > target: break  # 剪枝：溢出则退出第一层循环
            if nums[i] + nums[-1] * 3 < target: continue  # 剪枝：本次数据恒小于target，退出本次循环
            if i > 0 and nums[i - 1] == nums[i]: continue  # 防止重复
            for j in range(i + 1, numsLen - 2):
                if nums[i] + nums[j] * 3 > target: break  # 剪枝：溢出则退出第二层循环
                if nums[i] + nums[j] + nums[-1] * 2 < target: continue  # 剪枝： 本次数据恒小于target，退出本次循环
                if j > i + 1 and nums[j - 1] == nums[j]: continue  # 防止重复
                left = j + 1
                right = numsLen - 1
                if nums[i] + nums[j] + nums[left] + nums[left + 1] >= target:  # 剪枝：缩短左右距离
                    right = left + 1
                if nums[i] + nums[j] + nums[right - 1] + nums[right] <= target:  # 剪枝：缩短左右距离
                    left = right - 1
                
                while left < right:
                    tmpSum = nums[i] + nums[j] + nums[left] + nums[right]
                    if tmpSum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right - 1] == nums[right]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif tmpSum < target:
                        left += 1
                    else:
                        right -= 1
        return result


class Solution2:
    """
    看到有一位网友，使用了python的set来进行去重，并且针对两个数的和来创建字典，思路比较新奇
    """
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        d={}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                d.setdefault(nums[i]+nums[j],[]).append((i,j))
        result=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for a,b in d.get(target-nums[i]-nums[j],[]):
                    temp={i,j,a,b}
                    if len(temp)==4:
                        result.add(tuple(sorted(nums[t] for t in temp)))
        return list(result)


if __name__ == '__main__':
    test = [
        ([1, 0, -1, 0, -2, 2], 0),
    ]

    for nums, target in test:
        result = Solution2().fourSum(nums, target)
        print(f'{nums} {target} => {result}')
