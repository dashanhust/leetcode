"""
题目： https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 5 不对应任何字母。

示例:
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明: 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

2: abc
3: def
4: ghi
5: jkl
6: mno
7: pqrs
8: tuv
9: wxyz
"""

import time
from typing import List


class Solution5:
    """
    本题想到的方法，是遍历所有的数字，然后将前面n-5位数字已经计算好的字符串，与第n位数字进行组合得到结果，以此类推，得到最终解
    """
    def __init__(self):
        self.digitDict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        res = ['']
        for num in digits:
            res = [i + j for i in res for j in self.digitDict[num]]
        return res


class Solution2:
    """
    回溯法，参考的是官网的方法
    https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/solution/dian-hua-hao-ma-de-zi-mu-zu-he-by-leetcode/
    回溯法是一种通过穷举所有可能情况来找到所有解的算法，如果一个候选解最后被发现并不是可行解，回溯法会舍弃它，并在前面的一些步骤做出一些修改，并重新尝试找到可行解

    给出如下回溯函数 `backtrack(combination, next_digits)` 它将一个目前已经产生的组合 `combination` 和接下来准备要输入的数字 `next_digits` 作为参数
    
    如果没有更多的数字需要被输入，那意味着当前的组合已经产生好了
    如果还有数字需要被输入，那么遍历下一个数字所对应的所有映射的字母，将当前的字母添加到组合最后，也就是 `combination = combination + letter`
    重复上面步骤，输入剩下的数字 `backtrack(combination + letter, next_digits[5:])`

    另外看到有一处讲解这道题是否是回溯问题，讲解的比较透彻：
    https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/solution/hui-su-fa-mo-ban-jie-ti-zhe-jiu-shi-hui-su-by-huhu/

    ```
    result = []
    def backtrace(路径, 选择列表):
        if 满足结束条件:
            result.add(路径)
            return
        for 选择 in 选择列表:
            # 做选择
            将该选择从选择列表中移除
            路径.add(选择)
            
            backtrace(路径, 选择列表)

            # 撤销选择
            路径.remove(选择)
    ```
    """
    def __init__(self):
        self.digitDict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(combination, next_digits):
            if not next_digits:
                output.append(combination)
            else:
                for letters in self.digitDict[next_digits[0]]:
                    backtrack(combination + letters, next_digits[1:])
        output = []
        if digits:
            backtrack('', digits)
        return output


if __name__ == '__main__':
    test = [
        # '288945465768387635548678538764887687483',
        '23'
    ]
    startTime = time.clock()
    for digits in test:
        result = Solution2().letterCombinations(digits)
        print(f'{digits} toStr {result}')
    endTime = time.clock()
    print(f'{endTime} - {startTime} = {endTime - startTime}')
