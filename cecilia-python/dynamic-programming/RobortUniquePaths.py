#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   RobortUniquePaths.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/24 16:05   cecilia      1.0        机器人方格行走的不同路径
问题描述：一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路分析：
机器人每次只能向下或者向右走，那么分解到每一小格，机器人分别向下和向右行走的路径种数是总的情况
    1.首先确定状态转移数组，一般是二维数组，也就是定义 dp[i] [j]的含义为：当机器人从左上角走到(i, j) 这个位置时，一共有 dp[i] [j] 种路径。
    2.初始化数组,找出所有的初始化值。
    3.找出关系数组元素间的关系式。dp[i][j] = dp[i-1][j] + dp[i][j-1]
    4.转移过程以及边界条件的判断。

注意：这个网格相当于一个二维数组，数组是从下标为 0 开始算起的，所以 右下角的位置是 (m-1, n - 1)，所以 dp[m-1] [n-1] 就是我们要找的答案。
"""


def robortUniquePaths(m: int, n: int) -> int:
    """
    统计机器人行走的路径总和
    :param m: m行
    :param n: n列
    :return:
    算法分析：时间复杂度O(m*n)
    """
    # 判断边界条件
    if m <= 0 or n <= 0:
        return 0
    # 确定状态转移数组并初始化所有值
    dp = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    # 状态转移过程
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    # 终点位置为m-1，n-1
    return dp[m - 1][n - 1]


if __name__ == '__main__':
    print(robortUniquePaths(m=8, n=6))
