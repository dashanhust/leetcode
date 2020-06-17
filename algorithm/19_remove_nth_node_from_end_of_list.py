"""
题目: https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/

给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：给定的 n 保证是有效的。

进阶：你能尝试使用一趟扫描实现吗？
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return f'ListNode[{self.val}]'


class Solution1:
    """
    通过空间换取时间，首先一遍遍历完链表所有的元素，并且将所有元素的下标进行了记录，就是新创建的列表的下表
    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        tmpNodes = []
        while head:
            tmpNodes.append(head)
            head = head.next
        if n == len(tmpNodes): return tmpNodes[0].next
        tmpNodes[len(tmpNodes) - n - 1].next = tmpNodes[len(tmpNodes) - n].next

        return tmpNodes[0]


class Solution2:
    """
    参考官网提供的答案
    https://leetcode-cn.com/problems/two-sum/solution/liang-shu-zhi-he-by-leetcode-2/
    
    通过两个指针来进行遍历链表，这两个指针的距离是n，就是说前面的指针比后面的指针先走n步，这样当前面的指针遍历完的时候，后面的指针就是倒数第n个元素
    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for _ in range(n + 1):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next


class Solution3:
    """
    采用递归的思路，这里是一位网友的解法
    此时，我们可以将 removeNthFromEnd 理解为 getRealNode 即通过head来获取实际的节点信息
    由于递归的思路，是从最尾部开始计算的，所以当递归的次数 self._cur 等于 n 的时候，就返回此时 head.next 否则还是返回head
    """
    def __init__(self):
        self._cur = 0
    
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head: return None
        head.next = self.removeNthFromEnd(head.next, n)
        self._cur += 1
        if self._cur == n: return head.next
        return head




if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    # nums = [1]
    head = ListNode(nums[0])
    tmp = head
    for i in nums[1:]:
        tmp.next = ListNode(i)
        tmp = tmp.next
    nth = 5
    result = Solution3().removeNthFromEnd(head, nth)
    while result:
        print(f'{result} ->',end='')
        result = result.next
    print('')
