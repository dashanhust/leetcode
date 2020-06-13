"""
内容：给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
环境：python3.6
例子：
nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sort_num = sorted(enumerate(nums), key=lambda x: x[1])
        len_nums = len(nums)
        first = second = None
        for idx, item in enumerate(sort_num):
            first = item
            delta_num = target - first[1]
            index_start = idx + 1
            index_stop = len_nums - 1
            while index_start <= index_stop:
                index_half = (index_start + index_stop) // 2
                if delta_num == sort_num[index_half][1]:
                    second = sort_num[index_half]
                    break
                elif delta_num > sort_num[index_half][1]:
                    index_start = index_half + 1
                else:
                    index_stop = index_half - 1
            if second:
                break
        print(f'{first} + {second} = {target}')
        return [first[0], second[0]]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    result = Solution().twoSum(nums, target)
    print(result)
