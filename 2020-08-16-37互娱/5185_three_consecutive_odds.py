"""
题目：给你一个整数数组 arr，请你判断数组中是否存在连续三个元素都是奇数的情况：如果存在，请返回 true ；否则，返回 false 。

 

示例 1：

输入：arr = [2,6,4,1]
输出：false
解释：不存在连续三个元素都是奇数的情况。
示例 2：

输入：arr = [1,2,34,3,4,5,7,23,12]
输出：true
解释：存在连续三个元素都是奇数的情况，即 [5,7,23] 。
 

提示：

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
"""

import time
from typing import List


class Solution1:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        oddsNum = 0
        for item in arr:
            if item & 1 == 1:
                oddsNum += 1
                if oddsNum == 3:
                    return True
            else:
                oddsNum = 0
        return False


if __name__ == "__main__":
    test = [
        [2,6,4,1],  # false
        [1,2,34,3,4,5,7,23,12],  # true
    ]
    start = time.perf_counter()
    for arr in test:
        result = Solution1().threeConsecutiveOdds(arr)
        print(f'{arr} => {result}')
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
