#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   RobortUniquePathsII.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/29 16:25   cecilia      1.0        机器人走网格，遇到障碍物，统计总共有多少条不同的路径
问题描述；
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

注意：网格中的障碍物和空位置分别用 1 和 0 来表示。
说明：m 和 n 的值均不超过 100。

示例 1:
输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


def robortUniquePathsII(obstacleGrid: List[List[int]]) -> int:
    """
    遇到障碍物的情形下机器人所走的不同路径和
    思路分析：这种问题和I问题有所不同，第一种情形是网格中没有障碍物，路径可以随时选择。
        在具有障碍物的情况下，需要判断每一步是否具有障碍物，即obstacleGrid[i][j]==1,其他的逻辑和第一种情形下差不多。
    :param obstacleGrid:
    :return:
    算法分析：时间复杂度O(nm),空间复杂度O(1)
    """
    if not obstacleGrid:
        return 0

    m = len(obstacleGrid)  # 总行数
    n = len(obstacleGrid[0])  # 总列数

    dp = [[0 for _ in range(n)] for _ in range(m)]

    # 初始化的时候需要注意障碍物
    for i in range(1, m):
        # 遍历第一列时，判断是否存在障碍物，如果存在障碍物，不行走，否则继续行走
        if obstacleGrid[i][0] == 0:
            dp[i][0] = 1

    for j in range(n):
        if obstacleGrid[0][j] == 0:
            dp[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 0:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        print(dp)

    return dp[m - 1][n - 1]


def maxSubArray(nums: List[int]) -> int:
    if not nums:
        return 0
    maxSum = currentSum = nums[0]
    for i in range(1, len(nums)):
        # 每次求取的当前和需要和当前的值相比较，取最大
        currentSum = max(nums[i], nums[i] + currentSum)
        maxSum = max(currentSum, maxSum)

    return maxSum


if __name__ == '__main__':
    # print(robortUniquePathsII(obstacleGrid=[[0, 0, 0],
    #                                         [0, 1, 0],
    #                                         [0, 0, 0]]))

    print(robortUniquePathsII(obstacleGrid=[[0, 0], [1, 1], [0, 0]]))
    print(maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4]))
