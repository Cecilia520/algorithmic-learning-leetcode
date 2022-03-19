#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   NumIslands.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/5 16:39   cecilia      1.0         海岛岛屿的数量
问题描述：
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。
你可以假设网格的四个边均被水包围。

示例 1:

输入:
11110
11010
11000
00000

输出: 1
示例 2:

输入:
11000
11000
00100
00011

输出: 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def __init__(self):
        self.count = 0

    def getNumIslandsCount(self, grid: List[List[int]]) -> int:
        """
        统计岛屿的数量
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
                    self.count += 1
                backtrack(grid, i, j)
        return self.count


if __name__ == '__main__':
    s = Solution()
    print(s.getNumIslandsCount(grid=[[1, 1, 0, 0, 0],
                                     [1, 1, 0, 0, 0],
                                     [0, 0, 1, 0, 0],
                                     [0, 0, 0, 1, 1]]))
