"""
题目：给你一棵二叉搜索树，请你返回一棵 平衡后 的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。

如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是 平衡的 。

如果有多种构造方法，请你返回任意一种。

示例：
输入：root = [1,null,2,null,3,null,4,null,null]
输出：[2,1,3,null,null,null,4]
解释：这不是唯一的正确答案，[3,1,4,null,2,null,null] 也是一个可行的构造方案。
 

提示：
树节点的数目在 1 到 10^4 之间。
树节点的值互不相同，且在 1 到 10^5 之间。
"""

import time
from typing import List
import math


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def createTreeByNums(nums):
        nodes = []
        unVisited = []
        nodeNums = 0
        for idx, item in enumerate(nums):
            if item:
                nodes.append(TreeNode(item))
            # 获取该节点的父节点
            parentNodes = [i for i in unVisited if i[1] < 2]
            if parentNodes:
                parent = parentNodes[0]
                unVisited[parent[0]][1] += 1
                if item:
                    if parent[1] == 0:
                        nodes[parent[0]].left = nodes[-1]
                    else:
                        nodes[parent[0]].right = nodes[-1]
            if item:
                unVisited.append([nodeNums, 0])  # 表示没有遍历该节点的左右节点
                nodeNums += 1

        return nodes[0] if nodes else None

    @classmethod
    def printAllNodes(cls, nodes):
        result = []
        result.append(nodes.val)
        if nodes.left:
            result.extend(cls.printAllNodes(nodes.left))
        else:
            result.append(None)
        if nodes.right:
            result.extend(cls.printAllNodes(nodes.right))
        else:
            result.append(None)
        return result


class Solution1:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def getNums(treeRoot):
            if not treeRoot: 
                return []
            else:
                nums = [treeRoot.val]

            if treeRoot.left:
                nums = getNums(treeRoot.left) + nums
            if treeRoot.right:
                nums = nums + getNums(treeRoot.right)
            return nums
        
        def balance(left, right):
            if left > right: return None

            midIndex = (left + right) // 2
            root = TreeNode(treeNums[midIndex])
            if left < midIndex:
                root.left = balance(left, midIndex - 1)
            if midIndex < right:
                root.right = balance(midIndex + 1, right)
            return root

        # print(f'root: {root}')
        treeNums = getNums(root)
        # print(f'treeNums: {treeNums}')
        balanceRoot = balance(0, len(treeNums) - 1)
        # print(f'balanceRoot: {balanceRoot}')
        return balanceRoot


class Solution2:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        """
        这里参考了官网的解法，是对二叉搜索树进行了一次中序遍历，这样可以得到一个递增的有序数组
        然后针对有序数组，执行二分拆解，得到平衡二叉搜索树
        """
        def getInorder(o):
            if o.left:
                getInorder(o.left)
            inorderSeq.append(o.val)
            if o.right:
                getInorder(o.right)
        
        def build(left, right):
            midIndex = (left + right) // 2
            o = TreeNode(inorderSeq[midIndex])
            if left < midIndex:
                o.left = build(left, midIndex - 1)
            if midIndex < right:
                o.right = build(midIndex + 1, right)
            return o

        inorderSeq = []
        getInorder(root)
        return build(0, len(inorderSeq) - 1)


if __name__ == "__main__":
    test = [
        [1, None, 2, None, 3, None, 4, None, None],  # [2,1,3,null,null,null,4]
    ]
    start = time.perf_counter()
    for nums in test:
        iTreeRoot = TreeNode.createTreeByNums(nums)
        print(f'{nums} to TreeNodes => {TreeNode.printAllNodes(iTreeRoot)}')
        result = Solution1().balanceBST(iTreeRoot)
        print(f'BalanceBST=> {TreeNode.printAllNodes(result)}')
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
