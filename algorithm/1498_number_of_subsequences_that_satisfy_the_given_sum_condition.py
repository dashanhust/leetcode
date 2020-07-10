"""
题目：https://leetcode-cn.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

给你一个整数数组 nums 和一个整数 target 。

请你统计并返回 nums 中能满足其最小元素与最大元素的 和 小于或等于 target 的 非空 子序列的数目。

由于答案可能很大，请将结果对 10^9 + 7 取余后返回。

示例 1：
输入：nums = [3,5,6,7], target = 9
输出：4
解释：有 4 个子序列满足该条件。
[3] -> 最小元素 + 最大元素 <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)

示例 2：
输入：nums = [3,3,6,8], target = 10
输出：6
解释：有 6 个子序列满足该条件。（nums 中可以有重复数字）
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]

示例 3：
输入：nums = [2,3,3,4,6,7], target = 12
输出：61
解释：共有 63 个非空子序列，其中 2 个不满足条件（[6,7], [7]）
有效序列总数为（63 - 2 = 61）

示例 4：
输入：nums = [5,2,4,1,7,6,8], target = 16
输出：127
解释：所有非空子序列都满足条件 (2^7 - 1) = 127
 

提示：
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
1 <= target <= 10^6
"""

import time
from typing import List
import bisect


class Solution1:
    """
    先对数组排序
    然后针对每个元素作为起始元素算起，往后数数字，能够到达的最远数据，答案就是 2^(k-1) (假设子数组的最大长度为k)
    """
    def numSubseq(self, nums: List[int], target: int) -> int:
        lenNums = len(nums)
        nums.sort()
        ans = 0

        for left in range(lenNums):
            if nums[left] * 2 > target: break
            for right in range(left, lenNums):
                if nums[left] + nums[right] > target: break
            if nums[left] + nums[right] > target:
                right -= 1
            leftCount = pow(2, right - left)
            if right == left:
                leftCount = 1
            ans += leftCount
            # print(f'left: {left}; right: {right}, leftCount: {leftCount}')
                
        return ans % (10 ** 9 + 7)


class Solution2:
    """
    官方参考：https://leetcode-cn.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/solution/man-zu-tiao-jian-de-zi-xu-lie-shu-mu-by-leetcode-s/
    先排序，然后针对每一个元素作为最小值的情况下，能够得到的最多的最大值的情况，从而计算出这个最小值对于答案的贡献值
    另外计算摩的小技巧：
    (A + B) % P = ((A % P) + (B % P)) % P
    (A * B) % P = ((A % P) * (B % P)) % P
    """
    def numSubseq(self, nums: List[int], target: int) -> int:
        lenNums = len(nums)
        nums.sort()
        ans = 0
        fPower, twoPower =[], 1
        p = 10 ** 9 + 7

        # 获取各种下表元素的贡献值，例如假设最小值与最大值的距离为 i 那么这个最小值对于答案的贡献值就为 2^i
        for _ in range(lenNums):
            fPower.append(twoPower)
            twoPower <<= 1

        for left, val in enumerate(nums):
            # 以left作为最小值，为了方便的找到最大值 target - left 的位置下表，这里我们使用一个小技巧
            # 找到 target - left 的bisect_right位置然后再减去1，主要是为了让所有等于 target - left 的元素也能够包含在窗口中
            if (val << 1) > target: break
            right = bisect.bisect_right(nums, target - val) - 1
            ans  += fPower[right - left] % p
        return ans % p


class Solution3:
    """
    双指针法 时间复杂度 O(n * logn) 空间复杂度 O(n)
    参考：https://leetcode-cn.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/solution/python-pai-xu-shuang-zhi-zhen-by-irruma/
    """
    def numSubseq(self, nums: List[int], target: int) -> int:
        lenNums = len(nums)
        nums.sort()
        ans = 0
        fPower, twoPower = [], 1
        p = 10 ** 9 + 7

        # 获取各种下表元素的贡献值，例如假设最小值与最大值的距离为 i 那么这个最小值对于答案的贡献值就为 2^i
        for _ in range(lenNums):
            fPower.append(twoPower)
            twoPower <<= 1

        # 双指针法，左指针在列表的最左侧；右指针在列表的最右侧；分别从两端遍历
        # 如果相加和大于target，那么右指针左移（不符合要求）
        # 否则说明符合要求，然后寻找下一个，即左指针右移动
        # 直到 左指针下表 > 右指针下表
        left, right = 0, lenNums - 1
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                ans += fPower[right - left] % p
                left += 1
        return ans % p


if __name__ == "__main__":
    test = [
        [[3,5,6,7], 9], # 4
        [[3,3,6,8], 10], #6
        [[2,3,3,4,6,7], 12], # 61
        [[5,2,4,1,7,6,8], 16], # 127
        [[14,4,6,6,20,8,5,6,8,12,6,10,14,9,17,16,9,7,14,11,14,15,13,11,10,18,13,17,17,14,17,7,9,5,10,13,8,5,18,20,7,5,5,15,19,14],
22], # 272187084
    ]
    start = time.perf_counter()
    for (nums, target) in test:
        result = Solution3().numSubseq(nums, target)
        print(f'nums: {nums}; target: {target}; result: {result}')
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
