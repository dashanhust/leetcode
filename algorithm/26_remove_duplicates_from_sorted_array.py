"""
题目：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

 
示例 1:
给定数组 nums = [1,1,2], 
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 

你不需要考虑数组中超出新长度后面的元素。

示例 2:
给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。
 

说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""

import time
from typing import List


class Solution1:
    """
    采用双指针法，快指针在遍历数组的时候，如果值大于慢指针当前的值，那么就让慢指针下一个值设置为快指针当前的值
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = -1
        for item in nums:
            if ans == -1 or nums[ans] < item:
                ans += 1
                nums[ans] = item
        return ans + 1


class Solution2:
    """
    双指针法：两个指针同时向前运行，慢的指针表示最后的答案，快的指针用于遍历完整个原始数组
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0

        i = 0
        lenNums = len(nums)
        for j in range(1, lenNums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1


if __name__ == "__main__":
    test = [
        [1, 1, 2], # 2
        [0,0,1,1,1,2,2,3,3,4], # 5
    ]
    start = time.perf_counter()
    for item in test:
        result = Solution2().removeDuplicates(item)
        print(f'{item} => {result}')
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
