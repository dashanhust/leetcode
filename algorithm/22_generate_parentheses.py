"""
题目： https://leetcode-cn.com/problems/generate-parentheses/

数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例：
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
"""

from typing import List


class Solution1:
    """
    分别用left和right标记左括号和右括号的个数，每次从left和right里面抽取一个元素，并且要保证left的值必须 小于等于 right的值，直到left和right的值为0  left <= right
    可以想下是否可用回溯算法来求解
    
    此处回溯法的关键是要对选择列表进行设置，这里设置为 ['(', ')']
    """
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(combination, left, right):
            if left == right == 0:
                output.append(combination)
                return

            for i in ['(', ')']:
                if i == '(' and 0 < left <= right:
                    backtrack(combination + '(', left - 1, right)
                elif i == ')' and left <= right and right > 0:
                    backtrack(combination + ')', left, right - 1)    

        output = []
        backtrack('', n, n)
        return output


class Solution2:
    """
    看到网上以为网友的深度优先搜索算法DFS(Depth First Search)，更加简介
    """
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(combination, left, right):
            if left == right == 0: 
                output.append(combination)
                return
            if left < 0 or right < 0 or left > right: return
            backtrack(combination + '(', left - 1, right)
            backtrack(combination + ')', left, right - 1)

        output = []
        backtrack('', n, n)
        return output


if __name__ == "__main__":
    n = 3
    result = Solution2().generateParenthesis(n)
    print(f'{n} => {result}')
    # for i in result:
    #     print(f'{i}')
