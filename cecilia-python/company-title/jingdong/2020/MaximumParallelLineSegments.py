#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MaximumParallelLineSegments.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/18 22:38   cecilia      1.0       最多平行线段数目
问题描述：
给出平面上的2n个点，你可以将这个2n个点每两个匹配到一起得到n条线段吗？请你计算一种匹配方式，使得你得到的这两个线段平行的线段对数最多。

输入描述：第一行包含一个整数2n，接下来2n行，每行包含两个整数x和y，表示一个点的坐标；保证每个点都不重合，并且没有三点共线的情况。
输出描述：最多平行线端的对数

示例：
输入
>>
8
0 0
0 5
2 2
2 7
3 -2
5 0
4 -2
8 2

输出：
>> 6

解释：最多可以画出四条两两相互平行的线段，结果为C(2,4) = 6


思路分析：刚看到这个题目的时候，最初的想法就是两两选取两个点计算斜率，然后将计算的斜率的值存储在哈希表中，并记录每种斜率出现的次数。
如果点的数目过多的话，那么可能会产生很多空间开销，但是时间紧急，目前只想到这种策略，但是考后看到有人提供可以使用回溯的方法来做。
这在一定程度上可以减少空间的浪费，但是会增加计算时间开销。
"""
import collections


class Solution:
    def getGreatestCommonDivisor(self, y_diff, x_diff):
        """
        计算最大公约数，获得质分数
        :param y_diff:
        :param x_diff:
        :return:
        """
        divisor = y_diff % x_diff
        if divisor == 0:
            return x_diff
        else:
            return self.getGreatestCommonDivisor(x_diff, divisor)

    def getMaximumParallelLineSegments(self, n, points):
        """
        寻找最多的平行线的线段对数
        :param n: 点的个数
        :param points: 点集合
        :return:
        算法分析：时间复杂度O（N^2）
        """
        if not n or n < 0:
            return 0
        k_dict = collections.defaultdict(list)  # 哈希表，存储每个斜率的值和对应出现次数
        for i in range(n-1):
            for j in range(i + 1, n):
                y_diff = points[i][1] - points[j][1]
                x_diff = points[i][0] - points[j][0]
                x, y = 0, 0
                if y_diff == 0:
                    y = y
                    x = x
                elif x_diff == 0:
                    x = float('inf')
                    y = float('inf')
                else:
                    # 计算最大公约数来获得质分数
                    gcb = self.getGreatestCommonDivisor(y_diff, x_diff)
                    y = y_diff / gcb
                    x = x_diff / gcb

                if (y, x) not in k_dict.keys():
                    k_dict.setdefault((y, x), 1)
                else:
                    k_dict[(y, x)] += 1
        max_count = max(k_dict.values())
        return  (max_count * (max_count - 1)) // 2


if __name__ == '__main__':
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append([x, y])
    print(points)
    s = Solution()
    max_count = s.getMaximumParallelLineSegments(n, points)
    print(max_count)
