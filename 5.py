#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   5.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/9/8 18:53   cecilia      1.0         None
题目描述：
已知矩形的行和列，请按如下规律输出斜对角矩形。

例1：

输入：2 2

输出：[[1,3],[2,4]]

例2：

输入：1 2

输出：[[1, 2]]

输入：4 3

[[1, 3, 6], [2, 5, 9], [4, 8, 11], [7, 10, 12]]
"""
from typing import List
class Solution:
    def printLevel(self, matrix, tr, tc, dr, dc, flag):
        if flag is False:
            while dr != tr-1:
                dr -= 1
                dc += 1
        else:
            while tr != dr + 1:
                tr += 1
                tc -= 1

    def printMatrix(self, rows, cols, matrix: List[List[int]]) -> List[List[int]]:
        """
        按照要求打印矩阵
        :param row:
        :param col:
        :param matrix:
        :return:
        """
        tc, tr, dr, dc = 0, 0, 0, 0
        end_row, end_col = len(matrix) - 1, len(matrix[0]) - 1
        flag = False
        while tr != end_row + 1:
            self.printMatrix(matrix, tr, tc, dr, dc, flag)
            tr += 1 if tc == end_col else tr
            tc = tc if tc == end_col else tc + 1
            dc = dc + 1if dr == end_row else dc
            dr = dr if dr == end_row else dr + 1

            flag = not flag




if __name__ == '__main__':
    s = Solution()
    m, n = int(input().strip().split()[0]), int(input().strip().split()[1]) # 矩阵的行列大小
    for i in range(m):
        for j in range(n):
            pass

