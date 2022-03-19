#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   12.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/9/16 20:17   cecilia      1.0         None
"""
class Solution:
    def minSteps(self,matrix):
        """
        迷宫寻宝，寻找最大价值和最小步数
        0-道路， -1：起点，-2陷阱
        :param matrix:
        :return:
        """
        # define six directions
        # directions = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
        m = len(matrix)
        n = len(matrix[0])

        # start_x, start_y, end_x, end_y = -1, -1, -1, -1
        #
        # a = []
        # b = []

        dp = [[0 for _ in range(n)]for _ in range(m)]
        for i in range(1, m):
            if matrix[i][0] >= 0:
                dp[i][0] = dp[i - 1][0] + matrix[i][0]

        for i in range(1, n):
            if matrix[0][i] >= 0:
                dp[0][i] = dp[0][i - 1] + matrix[0][i]

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] > 0:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
        return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    input_list = input().strip().split()
    m, n, l = int(input_list[0]), int(input_list[1]), int(input_list[2])
    matrix = []
    for _ in range(m*l):
        tmp_list = list(map(int, input().strip().split()))
        matrix.append(tmp_list)
    print(s.minSteps(matrix))