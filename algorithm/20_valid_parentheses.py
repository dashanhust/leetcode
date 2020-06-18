"""
题目： https://leetcode-cn.com/problems/valid-parentheses/

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

示例 3:
输入: "(]"
输出: false

示例 4:
输入: "([)]"
输出: false

示例 5:
输入: "{[]}"
输出: true
"""


class Solution1:
    """
    采取栈的方式来求解
    左括号类型插入栈，如果遇到右括号，那么就从栈里面取最后一个元素来与当前右括号进行配对，如果不能配对，则失败
    直到遍历完所有字符串，如果栈为空，说明整个字符串配对成功，否则失败
    """
    def isValid(self, s: str) -> bool:
        parenthesesQueue = []
        parenthesesDict = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for item in s:
            if item == '':
                continue
            elif item in ['(', '{', '[']:
                parenthesesQueue.append(item)
            elif not parenthesesQueue or parenthesesDict[item] != parenthesesQueue.pop():
                return False
        return not parenthesesQueue


if __name__ == '__main__':
    test = [
        '()',  # true
        '()[]{}',  # true
        '(]',  # false
        '([)]',  # false
        '{[]}'  # true
    ]
    for s in test:
        result = Solution1().isValid(s)
        print(f'{s} isValid: {result}')
