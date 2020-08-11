"""
题目：给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X
解释:

被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的
"""

import time
from typing import List


def printList(board):
    for i in board:
        iJoin= ' '.join(i)
        print(f'{iJoin}')

class Solution1:
    def solve(self, board: List[List[str]]) -> None:
        """
        通过查找到哪些为 O 的元素，来决定其余为 O 的元素不能为 X 来解决问题
        1. 找出所有为 O 的元素
        2. 找到边界 O
        3. 与边界 O 相连的不能为 X
        """
        invalidPosList, validPosList = set(), set()
        lenBoard = len(board)
        for i, iBoard in enumerate(board):
            widthBoard = len(iBoard)
            for j, item in enumerate(iBoard):
                if item == 'O':
                    # 在边界上的 O 元素是肯定不会为成为 X 的
                    if i in [0, lenBoard - 1] or j in [0, widthBoard - 1]: 
                        invalidPosList.update([(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)])
                    # 在非边界上的 O 元素保留希望，但是需要进一步处理
                    else:
                        validPosList.add((i, j))
        hasMoreInvalid = True
        while hasMoreInvalid:
            hasMoreInvalid = False
            tmpInvalidPosList = invalidPosList & validPosList
            validPosList = validPosList - tmpInvalidPosList
            if tmpInvalidPosList and validPosList:
                for i, j in tmpInvalidPosList:
                    invalidPosList.update([(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)])
                hasMoreInvalid = True
        
        for item in validPosList:
            board[item[0]][item[1]] = 'X'

        return None


if __name__ == "__main__":
    test = [
        [
            ['X', 'X', 'X', 'X'],  # ['X', 'X', 'X', 'X']
            ['X', 'O', 'O', 'X'],  # ['X', 'X', 'X', 'X']
            ['X', 'X', 'O', 'X'],  # ['X', 'X', 'X', 'X']
            ['X', 'O', 'X', 'X']   # ['X', 'O', 'X', 'X']
        ],
    ]
    start = time.perf_counter()
    for board in test:
        print(f'Before solve:')
        printList(board)
        Solution1().solve(board)
        print(f'After solve:')
        printList(board)
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
