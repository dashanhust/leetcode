"""
题目：https://leetcode-cn.com/problems/merge-two-sorted-lists/

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return f'ListNode[{self.val}]'




class Solution1:
    """
    归并排序的思维，通过相互比较当前值来引入当前最小值
    """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        tmp = result
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        if l1: tmp.next = l1
        if l2: tmp.next = l2

        return result.next


class Solution2:
    """
    使用递归的思路
    """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == '__main__':
    l1List = [1, 2, 4]
    l2List = [1, 3, 4]
    l1 = ListNode()
    l1Dummy = l1
    l2 = ListNode()
    l2Dummy = l2
    for i in l1List:
        l1Dummy.next = ListNode(i)
        l1Dummy = l1Dummy.next
    for i in l2List:
        l2Dummy.next = ListNode(i)
        l2Dummy = l2Dummy.next

    result = Solution2().mergeTwoLists(l1.next, l2.next)
    while result:
        print(f'{result} -> ', end='')
        result = result.next
    print()
