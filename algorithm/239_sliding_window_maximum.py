"""
题目：https://leetcode-cn.com/problems/sliding-window-maximum/

给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

进阶：你能在线性时间复杂度内解决此题吗？

示例:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

提示：
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
"""

import time
from typing import List
import bisect
from collections import deque

class Solution1:
    """
    采用双指针方法，左闭右开的方式
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        lenNums = len(nums)
        left, right = 0, k
        ans = []

        if lenNums < k: return ans

        while right < lenNums + 1:
            curMax = max(nums[left:right])
            ans.append(curMax)
            left += 1
            right += 1
        return ans


class Solution2:
    """
    采用双指针法，左闭右开的方式
    但是区别于方法1的地方在于，这里我们将维护一个排序好了的列表，通过插入（right增加）和删除（left增加）的方式来改变列表元素
    
    
    不要每次都使用max函数来查找最大值，比较耗时间，这里我们将最大值元素和最大值元素的下标的最大值给记录下来，例如
    k=4的情况，子数组 [1, 2, 3, 3] 我们就需要记录下最大值 3 和最大值3的下标的最大值 3（下标从0开始）
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        lenNums = len(nums)
        left, right = 0, k
        ans = []
        windowSorted = []

        if lenNums < k: return ans

        windowSorted = sorted(nums[:k])
        ans.append(windowSorted[-1])
        
        while right < lenNums:
            bisect.insort_left(windowSorted, nums[right])
            leftIndex = bisect.bisect_left(windowSorted, nums[left])
            del windowSorted[leftIndex]

            ans.append(windowSorted[-1])
            left += 1
            right += 1
        return ans


class Solution3:
    """
    单调双端队列，时间复杂度为 O(n)
    参考： https://www.bilibili.com/video/BV1YV411o7Gr/
    要维护一个单调双端队列的时候，队列的头部是最大值的索引，尾部是最小值的索引。
    区别于方法二，窗口每次在向右移动的时候，都需要找到插入的下表，然后再删除窗口左边的元素，最后提取队列的最大值
    该方法是考虑到了，新进队列的元素 X 在进入窗口的时候，如果窗口里有比该元素还要小的值 Y ，那么可以直接舍弃 Y ，因为窗口在向右不管怎么移动，这些 Y 由于比 X 都要小，
    肯定不会是最大值的，毕竟这些Y要比X先移出窗口

    为了维护一个固定长度的双端队列，长度为k，那么在什么情况下，需要删除队列头部的最大值呢？
    窗口向右移动的时候，要插入到队列的下标为 i ，那么最左侧要移出窗口的下标 i - k 。那么如果窗口中的最大值下标（队列头部的值）< i - k + 1 的话，那么就需要将这个最大值删除

    这里根据上面链接的博主提供的算法，列出维护单调双端队列的口诀：
    1. 头: 删除头部的最大值（在一定条件下）
    2. 尾: 根据篮球队队长原则，删除尾部所有比即将插入窗口的新元素还要小的值
    3. 尾: 新元素加入到队列尾部
    4. 头: 头部的元素之就是此时窗口的最大值，提取即可（保证窗口的长度已经是k了才可以取队列头部元素）
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        lenNums = len(nums)
        dq = deque()
        ans = []

        for i in range(lenNums):
            # 删除头部的最大值
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            # 删除尾部小于即将插入滑动窗口的元素的值
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            # 元素插入队尾
            dq.append(i)
            # 提取头部最大值
            if i - k + 1 >= 0:
                ans.append(nums[dq[0]])

        return ans


class Solution4:
    """
    方法3中窗口内存储的是下标，这样会浪费一些时间，这里我们采取存储数值的方式
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []

        for i, v in enumerate(nums):
            # 删除头部的最大值
            if i - k >= 0 and dq and dq[0] == nums[i - k]:
                dq.popleft()
            # 删除尾部小于当前插入值的数据
            while dq and dq[-1] < v:
                dq.pop()
            # 元素插入队尾
            dq.append(v)
            # 提取头部最大值
            if i - k + 1 >= 0:
                ans.append(dq[0])
        
        return ans


class Solution5:
    """
    根据新加入窗口的元素的值与之前窗口的最大值进行比较，这种情况在数组是一个从大到小的极端情况，时间复杂度比较高
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        lenNums = len(nums)
        ans = []
        lastMax = max(nums[:k])
        ans.append(lastMax)

        for i in range(k, lenNums):
            if nums[i] >= lastMax:
                ans.append(nums[i])
                lastMax = nums[i]
            else:
                if nums[i - k] == lastMax:  
                    lastMax = max(nums[i - k + 1:i + 1])
                ans.append(lastMax)
        return ans



if __name__ == "__main__":
    test = [
        [[1,3,-1,-3,5,3,6,7], 3], # [3,3,5,5,6,7]
        [[-7,-8,7,5,7,1,6,0], 4], # [7,7,7,7,7]
    ]
    start = time.perf_counter()
    for (nums, k) in test:
        result = Solution3().maxSlidingWindow(nums, k)
        print(f'nums: {nums}; k: {k}; result: {result}')
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
