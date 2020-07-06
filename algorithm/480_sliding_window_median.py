"""
题目：https://leetcode-cn.com/problems/sliding-window-median/

中位数是 有序序列 最中间的那个数。如果序列的大小是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。 注意这里是针对有序序列的最中间的数据，才是中位数

例如：

[2,3,4]，中位数是 3
[2,3]，中位数是 (2 + 3) / 2 = 2.5
给你一个数组 nums，有一个大小为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1 位。你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。

 

示例：

给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。

窗口位置                      中位数
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7      -1
 1  3 [-1  -3  5] 3  6  7      -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
 因此，返回该滑动窗口的中位数数组 [1,-1,-1,3,5,6]。

 

提示：

你可以假设 k 始终有效，即：k 始终小于输入的非空数组的元素个数。
与真实值误差在 10 ^ -5 以内的答案将被视作正确答案。
"""

import time
from typing import List
from collections import deque
import bisect


class Solution1:
    """
    暴力法
    针对窗口中的元素进行排序，然后获取排序后的窗口的中位数
    """
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        kDiv, kMod = divmod(k, 2)
        ans = []
        right, lenNums = k, len(nums)
        while right <= lenNums:
            sortedWindow = sorted(nums[right - k:right])
            if kMod == 1:
                ans.append(sortedWindow[kDiv])
            else:
                ans.append(sum(sortedWindow[kDiv - 1:kDiv]) / 2)
            right += 1
        return ans


class Solution2:
    """
    维持一个有序的队列
    """
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        kDiv, kMod = divmod(k, 2)
        lenNums = len(nums)
        window, ans = [], []
        
        for right in range(lenNums):
            left = right - k
            # 删除窗口left元素
            if left >= 0:
                idx = bisect.bisect_left(window, nums[left])
                del window[idx]
            # 插入窗口right元素
            bisect.insort_left(window, nums[right])
            # 获取中位数
            if left >= -1:
                if kMod == 1:
                    ans.append(window[kDiv])
                else:
                    ans.append(sum(window[kDiv - 1:kDiv + 1]) / 2)
        return ans


if __name__ == "__main__":
    test = [
        # [[1,3,-1,-3,5,3,6,7], 3],  # [1,-1,-1,3,5,6]
        [[1,4,2,3], 4], # [2.5]
    ]
    start = time.perf_counter()
    for (nums, k) in test:
        result = Solution2().medianSlidingWindow(nums, k)
        print(f'nums: {nums}; k: {k}; result: {result}')
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
