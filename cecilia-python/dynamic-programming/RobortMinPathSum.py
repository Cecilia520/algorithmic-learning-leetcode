#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   RobortMinPathSum.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/24 16:34   cecilia      1.0       网格最短路径和
问题描述：
提供一个MxN大小的网格，机器人每次只能向下走或者向右行走一步，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

https://leetcode-cn.com/problems/minimum-path-sum/
解决思路和上一道机器人所有路径之和的题型差不多，只是这个需要寻找最优子结构。
寻找最优子结构的思维：将所有情况分解成多个解集合P1，P2......Pn,如果P2,P3...Pn是最优的，那么最后的一定是最优的。
"""
from typing import List


def robortMinPathSum(grid: List[List[int]]) -> int:
    """
    寻找最优的路径和
    :param grid: 网格二维数组
    :return:
    算法分析：时间复杂度O(n*m),空间复杂度O(1)
    """
    m = len(grid)
    n = len(grid[0])

    # 判断边界情况
    if n <= 0 or m <= 0:
        return 0

    # 定义状态转移数组并初始化所有值
    dp = [[0 for _ in range(n)] for _ in range(m)]

    dp[0][0] = grid[0][0]

    # 初始化最左边的所有行值
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    # 初始化最上边的所有列值
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # 状态转移函数
    for i in range(1, m):
        for j in range(1, n):
            # 如果每一步都是最短的，那么最后累积得到的一定是最短的
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    return dp[m - 1][n - 1]


if __name__ == '__main__':
    # print(robortMinPathSum(grid=[[1, 3, 1],
    #                              [1, 5, 1],
    #                              [4, 2, 1]]))
    print(robortMinPathSum(grid=[[1]]))
