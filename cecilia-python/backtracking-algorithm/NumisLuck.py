#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   NumisLuck.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/23 19:21   cecilia      1.0         统计幸运星的个数
问题描述：给定一些星星的坐标，如果一个星星的左、右、上、下都存在星星（不一定是相邻的），那么该星星定义为幸运星。
示例：
8
0 0
0 1
0 2
0 3
1 1
1 2
-1 1
-1 2

输出：2
幸运星（0，2）和（0，1）
"""
import sys
from typing import List

class Solution:
    def __init__(self):
        self.count = 0

    def getNumIslandsCount(self, grid: List[List[int]]) -> int:
        """
        统计幸运星的数量
        常规思路：回溯法
        :param grid:
        :return:
        """
        def backtrack(grid, i, j):
            # 回溯终止条件
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
                return

            grid[i][j] = 0 # 当不满足终止条件时，需要在周围继续寻找，进入回溯

            backtrack(grid, i - 1, j)
            backtrack(grid, i + 1, j)
            backtrack(grid, i, j - 1)
            backtrack(grid, i, j + 1)

        if not grid or len(grid) <= 0:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # self.count += 1
                    backtrack(grid, i, j)


        return self.count



if __name__ == '__main__':
    n = int(input())
    input_list = []
    max_x = 0
    max_y = 0
    min_x = sys.maxsize
    min_y = 1001
    for i in range(n):
        x, y = map(int, input().split())
        max_x = max(max_x, x)
        min_x = min(min_x, x)
        max_y = max(max_y, y)
        min_y = min(min_y, y)
        input_list.append([x, y])
    print(input_list)

    grids = [[0 for _ in range(min_y, max_y+1)]for _ in range(min_x, max_x+1)]
    for i in range(min_x, max_x+1):
        for j in range(min_y, max_y+1):
            if [i, j] in input_list:
                grids[i][j] = 1
    s = Solution()
    res = s.getNumIslandsCount(grids)
    print(res)
