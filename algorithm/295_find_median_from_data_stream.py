"""
题目：https://leetcode-cn.com/problems/find-median-from-data-stream/

中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
进阶:

如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
"""

import time
from typing import List
import bisect
import heapq


class MedianFinder1:
    """
    采用二分查找的方法，维护一个栈
    """
    def __init__(self):
        self._dataStack = []

    def addNum(self, num: int) -> None:
        bisect.insort_left(self._dataStack, num)

    def findMedian(self) -> float:
        dataNum = len(self._dataStack)
        median = (self._dataStack[(dataNum - 1) // 2] + self._dataStack[dataNum // 2]) / 2
        return median


class MedianFinder2:
    """
    采用堆的方法，利用两个堆来维护这个窗口，两个堆都是最大堆
    
    self._min_heap 堆用于维护有序数组中的较大值部分，并且按照从小到大排列（最小堆）
    self._max_heap 堆用于维护有序数组中的较小值部分，并且按照从大到小（最大堆）

    两者的存储数据排列顺序之所以不同，是因为获取中位数，需要中的数据进行计算，当有序数组的长度为偶数时，需要拿两个堆的根元素进行求解平均值

    并且最小堆(self._min_heap)的长度 >= 最大堆(self._max_heap)的长度
    """
    def __init__(self):
        self._min_heap = []
        self._max_heap = []

    def addNum(self, num: int) -> None:
        if len(self._min_heap) == len(self._max_heap):
            heapq.heappush(self._min_heap, -heapq.heappushpop(self._max_heap, -num))
        else:
            heapq.heappush(self._max_heap, -heapq.heappushpop(self._min_heap, num))
    
    def findMedian(self) -> float:
        if len(self._min_heap) == len(self._max_heap):
            return (self._min_heap[0] - self._max_heap[0]) / 2
        else:
            return self._min_heap[0]


if __name__ == "__main__":
    obj = MedianFinder2()
    obj.addNum(1)
    obj.addNum(2)
    param_1 = obj.findMedian()
    obj.addNum(3)
    param_2 = obj.findMedian()
    print(f'{param_1} {param_2}')
