"""
题目：将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

二叉搜索树（Binary Search Tree(BST)）又称为二叉查找树或二叉排序树，它或者是一棵空树，或者是具有如下性质的二叉树：
1. 若它的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
2. 若它的右子树不空，则右子树上所有节点的值均大于他的根节点的值；
3. 它的左右子树也分别为二叉搜索树
"""

import time
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @classmethod
    def printAllNodes(cls, nodes):
        result = []
        result.append(nodes.val)
        if nodes.left:
            result.extend(cls.printAllNodes(nodes.left))
        if nodes.right:
            result.extend(cls.printAllNodes(nodes.right))
        return result


class Solution1:
    """
    将有序数组，通过中序遍历的划分方法，划分数组，数组左边的作为节点的左边节点，数组右边的作为节点的右边节点
    """
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None

        midIndex = len(nums) // 2
        root = TreeNode(nums[midIndex])
        if nums[:midIndex]:
            root.left = self.sortedArrayToBST(nums[:midIndex])
        if nums[midIndex + 1:]:
            root.right = self.sortedArrayToBST(nums[midIndex + 1:])
        return root


class Solution2:
    """
    方法1需要不断的创建新的数字，这样增加了空间复杂度，这里我们不使用中间数组，而是通过下标的方式来约束数组
    """
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None
            midIndex = (left + right) // 2
            root = TreeNode(nums[midIndex])
            if left < midIndex:
                root.left = helper(left, midIndex - 1)
            if midIndex < right:
                root.right = helper(midIndex + 1, right)
            return root
        return helper(0, len(nums) - 1)


if __name__ == "__main__":
    test = [
        [-10,-3,0,5,9]
    ]
    start = time.perf_counter()
    for nums in test:
        result = Solution1().sortedArrayToBST(nums)
        print(f'{nums} => {TreeNode.printAllNodes(result)}')
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
