"""
内容： 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
      如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
      您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
环境： python3.6
例子：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return f"({self.val}, {self.next})"


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        prenode = ListNode(0)
        lastnode = prenode
        val = 0
        while l1 and l2:
            val, cur = divmod(val + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10)
            lastnode.next = ListNode(cur)
            lastnode = lastnode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        l3 = l1 if l1 else l2

        if l3:
            while val and l3:
                val, cur = divmod(val + l3.val, 10)
                lastnode.next = ListNode(cur)
                lastnode = lastnode.next
                l3 = l3.next if l3 else None
            if l3:
                lastnode.next = l3
        if val:
            lastnode.next = ListNode(val)

        return prenode.next

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         l1Tmp = l1
#         l2Tmp = l2
#         tmpSum = l1.val + l2.val
#         newNode = ListNode(tmpSum % 10)
#         tmpSum = tmpSum // 10
#         tmpNode = newNode

#         l1Tmp = l1Tmp.next
#         l2Tmp = l2Tmp.next
#         while l1Tmp and l2Tmp:
#             tmpSum = tmpSum + l1Tmp.val + l2Tmp.val
#             tmpNode.next = ListNode(tmpSum % 10)
#             tmpNode = tmpNode.next
#             l1Tmp = l1Tmp.next
#             l2Tmp = l2Tmp.next
#             tmpSum = tmpSum // 10
#         if l1Tmp:
#             while l1Tmp and tmpSum:
#                 tmpSum = tmpSum + l1Tmp.val
#                 tmpNode.next = ListNode(tmpSum % 10)
#                 tmpNode = tmpNode.next
#                 l1Tmp = l1Tmp.next
#                 tmpSum = tmpSum // 10
#             if l1Tmp:
#                 tmpNode.next = l1Tmp
#         elif l2Tmp:
#             while l2Tmp and tmpSum:
#                 tmpSum = tmpSum + l2Tmp.val
#                 tmpNode.next = ListNode(tmpSum % 10)
#                 tmpNode = tmpNode.next
#                 l2Tmp = l2Tmp.next
#                 tmpSum = tmpSum // 10
#             if l2Tmp:
#                 tmpNode.next = l2Tmp
#         if tmpSum:
#             tmpNode.next = ListNode(tmpSum)
#         return newNode


def createNode(num: int) -> ListNode:
    num_copy = num
    remainder = num_copy % 10
    listNode = ListNode(remainder)
    tmpNode = listNode
    num_copy = num_copy // 10

    while num_copy % 10:
        remainder = num_copy % 10
        num_copy = num_copy // 10
        tmpNode.next = ListNode(remainder)
        tmpNode = tmpNode.next

    return listNode

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


if __name__ == '__main__':
    # num = 342
    # num_copy = num
    # remainder = num_copy % 10
    # listNode = ListNode(remainder)
    # tmpNode = listNode
    # num_copy = num_copy // 10

    # while num_copy // 10:
    #     remainder = num_copy % 10
    #     num_copy = num_copy // 10
    #     tmpNode.next = ListNode(remainder))
    #     tmpNode = tmpNode.next
    # else:
    #     tmpNode.next = ListNode(num_copy))
    # print(f'{num} list => {listNode}')
    num1 = 1
    num2 = 99
    tmpNode1 = createNode(num1)
    tmpNode2 = createNode(num2)
    print(f'{num1} => {tmpNode1}')
    print(f'{num2} => {tmpNode2}')

    sumNode = Solution().addTwoNumbers(tmpNode1, tmpNode2)
    print(f'{tmpNode1} + {tmpNode2} = {sumNode}')
    listNodeToString(sumNode)

