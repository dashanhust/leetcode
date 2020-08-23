"""
题目：给你一个整数 n 和一个整数数组 rounds 。有一条圆形赛道由 n 个扇区组成，扇区编号从 1 到 n 。现将在这条赛道上举办一场马拉松比赛，该马拉松全程由 m 个阶段组成。其中，第 i 个阶段将会从扇区 rounds[i - 1] 开始，到扇区 rounds[i] 结束。举例来说，第 1 阶段从 rounds[0] 开始，到 rounds[1] 结束。

请你以数组形式返回经过次数最多的那几个扇区，按扇区编号 升序 排列。

注意，赛道按扇区编号升序逆时针形成一个圆（请参见第一个示例）。

示例 1：
输入：n = 4, rounds = [1,3,1,2]
输出：[1,2]
解释：本场马拉松比赛从扇区 1 开始。经过各个扇区的次序如下所示：
1 --> 2 --> 3（阶段 1 结束）--> 4 --> 1（阶段 2 结束）--> 2（阶段 3 结束，即本场马拉松结束）
其中，扇区 1 和 2 都经过了两次，它们是经过次数最多的两个扇区。扇区 3 和 4 都只经过了一次。

示例 2：
输入：n = 2, rounds = [2,1,2,1,2,1,2,1,2]
输出：[2]

示例 3：
输入：n = 7, rounds = [1,3,5,7]
输出：[1,2,3,4,5,6,7]
 
提示：
2 <= n <= 100
1 <= m <= 100
rounds.length == m + 1
1 <= rounds[i] <= n
rounds[i] != rounds[i + 1] ，其中 0 <= i < m
"""

import time
from typing import List


class Solution1:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        if not rounds: return []

        lenR = len(rounds)
        visitedList = [0] * (n + 1) # 初始化每个赛道的次数为0 赛道的下表从1开始
        start = rounds[0]
        visitedList[start] += 1
        for i in range(1, lenR):
            cur = rounds[i] if start < rounds[i] else rounds[i] + n
            while start <= cur - 1:
                start += 1
                if start <= n:
                    visitedList[start] += 1
                else:
                    visitedList[start - n] += 1
            start = rounds[i]
        maxVisited = max(visitedList)
        targetVisisted = [idx for idx, val in enumerate(visitedList) if val == maxVisited]
        return targetVisisted


class Solution2:
    """
    简化思想：
    中间不论走了多少圈，每一圈对于每个扇区增加的次数都是1，所以只需要考虑起点和终点即可
    若 起点 < 终点；那么答案就是 [起点, ..., 终点]
    若 起点 = 终点；那么答案就是 [起点]
    若 起点 > 终点；那么答案就是 [1, ..., 起点, 终点, ..., n]

    其中 n 表示扇区的总数量
    """
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        start, end = rounds[0], rounds[-1]
        if start <= end:
            return list(range(start, end + 1))
        else:
            return list(range(1, end + 1)) + list(range(start, n + 1))


if __name__ == "__main__":
    test = [
        [4, [1,3,1,2]],  # [1,2]
        [2, [2,1,2,1,2,1,2,1,2]],  # [2]
        [7, [1,3,5,7]],  # [1,2,3,4,5,6,7]
        [2,[1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1]],  # [1]
        [3,[3,2,1,2,1,3,2,1,2,1,3,2,3,1]],  # [1, 3]
    ]
    start = time.perf_counter()
    for n, rounds in test:
        result = Solution2().mostVisited(n, rounds)
        print(f'{n}, {rounds} => {result}')
    end = time.perf_counter()
    print(f'TimeCost: {end} - {start} = {end - start}')
