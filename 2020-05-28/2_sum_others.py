"""
参考的别人填写内容
https://leetcode-cn.com/problems/two-sum/solution/ha-xi-zi-dian-kuai-su-cha-zhao-by-powcai/

采用哈希的方法
"""

from typing import List


class Solution:
    def twoSum(self, nums: List, target: int) -> List:
        n = len(nums)
        tmp = {}
        for idx, item in enumerate(nums):
            delta = target - item
            if delta in tmp.keys():
                return [idx, tmp[delta]]
            else:
                tmp[delta] = idx

