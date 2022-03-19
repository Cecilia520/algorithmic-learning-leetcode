#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   RobortMovingCount.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/5 14:59   cecilia      1.0        机器人运动的范围
问题描述：
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

思路分析：经典的回溯法。
将地图全部置1，遍历能够到达的点，将遍历的点置0并令计数+1.
"""


class Solution:
    def __init__(self):
        self.count = 0

    def getRobortMovingCount(self, rows, cols, threshold):
        """
        统计机器人运动范围，和leetcode上的海盗数量问题类似
        :param rows: 矩阵总行数
        :param cols: 矩阵总列数
        :param threshold: 阈值
        :return:
        """

        def backtrack(arr, i, j, threshold):
            """
            根据每个元素进行回溯判断
            :param arr: 初始化的路径数组
            :param i: 元素的索引行i
            :param j: 元素的索引列j
            :param threshold: 阈值
            :return:
            """
            # 回溯的终止条件:边界
            if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]):
                return
            # 回溯的终止条件：题意的条件
            tmpi = list(map(int, list(str(i))))
            tmpj = list(map(int, list(str(j))))
            if sum(tmpi) + sum(tmpj) > threshold or arr[i][j] != 1:
                return

            arr[0][0] = 0
            self.count += 1
            # 递归回溯
            backtrack(arr, i - 1, j, threshold)
            backtrack(arr, i + 1, j, threshold)
            backtrack(arr, i, j - 1, threshold)
            backtrack(arr, i, j + 1, threshold)

        arr = [1 for _ in range(cols) for _ in range(rows)]
        backtrack(arr, 0, 0, threshold)
        return self.count


import sys

if __name__ == '__main__':
    n = int(input())
    x_nums = list(map(int, input().split()))
    y_nums = list(map(int, input().split()))
    result = [sys.maxsize] * n
    for x in x_nums:
        for y in y_nums:
            dist_sum = 0
            # 遍历每个棋子点到其他棋子之前的距离，并排序
            dist_nums = sorted([abs(x - x_nums[i]) + abs(y - y_nums[i]) for i in range(n)])
            # 遍历每个棋子，比较得到距离和最小的
            for i in range(n):
                dist_sum += dist_nums[i]
                if dist_sum <= result[i]:
                    result[i] = dist_sum
    print(' '.join(map(str, result)))
