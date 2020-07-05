"""
题目：https://leetcode-cn.com/problems/min-stack/

设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。
 

示例:

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
 

提示：
pop、top 和 getMin 操作总是在 非空栈 上调用。
"""

import time
from typing import List


class MinStack1:
    
    def __init__(self):
        self._dataStack = []
        self._minStack = []

    def push(self, x: int) -> None:
        self._dataStack.append(x)
        tmpMin = x
        if self._minStack:
            tmpMin = min(self._minStack[-1], x)
        self._minStack.append(tmpMin)
            
    def pop(self) -> None:
        self._dataStack.pop()
        self._minStack.pop()

    def top(self) -> int:
        return self._dataStack[-1]

    def getMin(self) -> int:
        return self._minStack[-1]


class MinStack2:
    """
    由于需要在常量级别的时间复杂度中获取到最小值，所以这里我们采取用空间换取时间的方式，除了有数据栈外，还有辅助栈（存储最小值）

    当数据栈新添加的数据  >   辅助栈的top元素，那么辅助栈不需要处理
    当数据栈新添加的数据  <=  辅助栈的top元素，那么新数据需要压入到辅助栈中

    当数据栈弹出的top数据 == 辅助栈的top元素，那么辅助栈也要弹出top元素    
    """
    
    def __init__(self):
        self._dataStack = []
        self._minStack = []

    def push(self, x: int) -> None:
        self._dataStack.append(x)
        if not self._minStack or (self._minStack and x <= self._minStack[-1]):
            self._minStack.append(x)

    def pop(self) -> None:
        if self._dataStack[-1] == self._minStack[-1]:
            self._minStack[-1].pop()
        self._dataStack[-1].pop()

    def top(self) -> int:
        return self._dataStack[-1]

    def getMin(self) -> int:
        return self._minStack[-1]


class Node:
    def __init__(self, v=None, m=None):
        self.val = v
        self.min = m
        self.next = None


class MinStack3:
    """
    使用链表实现
    """
    def __init__(self):
        self._head = None

    def push(self, x: int) -> None:
        nodeMin = x
        if self._head and self._head.min < x:
            nodeMin = self._head.min
        tmpNode = Node(x, nodeMin)
        tmpNode.next = self._head
        self._head = tmpNode

    def pop(self) -> None:
        self._head = self._head.next

    def top(self) -> int:
        return self._head.val

    def getMin(self) -> int:
        return self._head.min


if __name__ == "__main__":
    obj = MinStack3()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    param_1 = obj.getMin()
    obj.pop()
    param_2 = obj.top()
    param_3 = obj.getMin()
    
    # -3 0 -2
    print(f'param_1: {param_1}; param_2: {param_2}, param_3: {param_3}')