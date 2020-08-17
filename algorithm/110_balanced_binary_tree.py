"""
题目：给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。
"""

import time
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def createTreeByList(nums):
        if not nums: return None
        root = TreeNode(nums[0])
        q = [[root, 0]]
        for item in nums[1:]:
            tmpNode = TreeNode(item) if item else None
            withoutSubTreeId = [idx for idx, node in enumerate(q) if node[1] < 2][0]
            if q[withoutSubTreeId][1] == 0:
                q[withoutSubTreeId][0].left = tmpNode
            else:
                q[withoutSubTreeId][0].right = tmpNode
            q[withoutSubTreeId][1] += 1

            if tmpNode:
                q.append([tmpNode, 0])
        return root

    def printAllNodes(self):
        result = [self.val]
        if self.left:
            result.extend(self.left.printAllNodes())
        if self.right:
            result.extend(self.right.printAllNodes())
        return result


class Solution1:
    """
    自顶向下的递归判断
    时间复杂度为 O(n^2); 空间复杂度为 O(n)
    """
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root: return 0
            return max(height(root.left), height(root.right)) + 1
        
        if not root: return True
        target = abs(height(root.left) - height(root.right)) <= 1 and \
            self.isBalanced(root.left) and \
            self.isBalanced(root.right)
        return target


class Solution2:
    """
    自底向上的递归判断:
    类似于后续遍历，对于当前遍历到的节点，先递归地判断其左右子树是否平衡，再判断以当前节点为根的子树是否平衡。
    如果一棵子树是平衡的，则返回其高度（高度一定是非负数）；
    否则返回 -1
    如果一棵子树不平衡，则整个二叉树不平衡

    时间复杂度为 O(n); 空间复杂度为 O(n)
    """
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root: return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1

        return height(root) >= 0


class Solution3:
    """
    方法1的自顶向下的递归判断，可以进行优化，在每次计算左右子树高度的时候，就判断左右子树是否是平衡树
    """
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root: return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if abs(leftHeight - rightHeight) > 1:
                flag[0] = False
            return max(leftHeight, rightHeight) + 1
        
        flag = [True]
        height(root)
        return flag[0]



if __name__ == "__main__":
    test = [
        [3,9,20,None,None,15,7],  # true
        [1,2,2,3,3,None,None,4,4],  # false
    ]
    start = time.perf_counter()
    for item in test:
        itemRoot = TreeNode.createTreeByList(item)
        result = Solution3().isBalanced(itemRoot)
        # print(f'{item} is balanced? {itemRoot.printAllNodes()}')
        print(f'{item} is balanced? {result}')
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
