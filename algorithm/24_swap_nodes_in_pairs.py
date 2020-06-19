"""
题目： https://leetcode-cn.com/problems/swap-nodes-in-pairs/

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
"""

import time
from typing import List


class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

    @classmethod
    def createNodes(cls, n: List[int]):
        result = cls()
        dummy = result
        for i in n:
            dummy.next = cls(i)
            dummy = dummy.next
        return result.next

    def __str__(self):
        dummy = self.next
        result = f'{self.val}'
        while dummy:
            result = f'{result} -> {dummy.val}'
            dummy = dummy.next
        return result


class Solution1:
    """
    通过将相邻的奇数节点与偶数节点进行交换，直到所有节点都已经交换完成
    但是需要注意避免陷入死循环中
    oddNode.next = None 即将奇数节点的next提前设置为None
    """
    def swapPairs(self, head: ListNode) -> ListNode:
        result = dummy = ListNode()
        while head:
            oddNode = head
            evenNode = head.next
            
            if evenNode:
                head = evenNode.next
                oddNode.next = None
                dummy.next = evenNode
                dummy = dummy.next
            else:
                head = oddNode.next
            dummy.next = oddNode
            dummy = dummy.next
        return result.next


if __name__ == "__main__":
    lists = [1, 2, 3, 4]
    lists = ListNode.createNodes(lists)
    start = time.perf_counter()
    result = Solution1().swapPairs(lists)
    print(f'{result}')
    end = time.perf_counter()
    print(f'{end} - {start} = {end - start}')
