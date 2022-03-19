#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   CalMaxPathNum.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/9/15 18:59   cecilia      1.0        米兔吃胡萝卜，计算最大胡萝卜数目
"""
from typing import List


class Solution:
    def calMaxNum(self, matrix: List[List[int]], m: int, n: int) -> int:
        """
        统计胡萝卜的最大数目
        :param matrix: 输入矩阵
        :param m 矩阵的行数
        :param n 矩阵的列数
        :return:
        """
        if not m and not n:
            return 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = matrix[0][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + matrix[0][j]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + matrix[i][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]
        return dp[-1][-1]

    def calMaxNum2(self, matrix: List[List[int]], m: int, n: int) -> int:
        """
        统计胡萝卜的最大数目(空间优化)
        :param matrix: 输入矩阵
        :param m 矩阵的行数
        :param n 矩阵的列数
        :return:
        """
        if not m and not n:
            return 0
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                elif i == 0:
                    matrix[i][j] = matrix[i][j - 1] + matrix[i][j]
                elif j == 0:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j]
                else:
                    matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1]) + matrix[i][j]
        return matrix[-1][-1]


if __name__ == '__main__':
    s = Solution()
    input_list = input().strip().split()
    m, n = int(input_list[0]), int(input_list[1])
    matrix = []
    for i in range(m):
        tmp_list = list(map(int, input().strip().split()))
        matrix.append(tmp_list)
    print("matrix:{}".format(matrix))
    print(s.calMaxNum(matrix, m, n))
    print("-----------2------------")
    print(s.calMaxNum2(matrix, m, n))
