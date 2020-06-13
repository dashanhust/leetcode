"""
题目：你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
      给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
环境：python3.6
样例：
    输入: [1,2,3,1]
    输出: 4
    解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
         偷窃到的最高金额 = 1 + 3 = 4 。

本案例采用动态规划的方式，需要写出状态转移方程，为了减少空间，可以采用滚动数组的方法
当 n = 0 时，最大值 S0 为 0
当 n = 1 时，最大值 S1 为 nums[0]
当 n = 2 时，最大值 S2 为 max(S1, S0 + nums[1]) => max(nums[0], 0 + nums[1])
总结规律
Sn = max(S(n-1), S(n-2) + nums[n])
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # len_nums = len(nums)
        # first = 0
        # if len_nums == 0:
        #     return first
        # second = nums[0]
        # for i in range(1, len_nums):
        #     first, second = second, max(second, first + nums[i])
        # return second

        first = second = 0
        for item in nums:
            first, second = second, max(second, first + item)
        return second

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         max_sum = 0
#         sorted_nums = sorted(enumerate(nums), key=lambda x: x[1], reverse=True)
#         len_nums = len(nums)
#         for i in range(len_nums):
#             pos_list = []
#             for idx, num in sorted_nums[i:]:
#                 delta_idx = [abs(item[0] - idx) == 1 for item in pos_list]

#                 if not any(delta_idx):
#                     pos_list.append((idx, num))
#             pos_sum = sum([item[1] for item in pos_list])
#             max_sum = max(max_sum, pos_sum)
#         return max_sum

if __name__ == '__main__':
    # input = [1,2,3,1]
    # input = [2,7,9,3,1]
    # input = [2,3,2]
    # input = [8,2,8,9,2]
    input = [8,9,9,4,10,5,6,9,7,9]
    result = Solution().rob(input)
    print(f'{input} max sum: {result}')
