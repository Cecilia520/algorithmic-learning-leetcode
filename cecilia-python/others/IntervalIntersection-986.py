#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   IntervalIntersection-986.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/12 11:55   cecilia      1.0       区间列表的交集（应用可参考1229）
问题描述：
给定两个由一些闭区间组成的列表，每个区间列表都是成对不相交的，并且已经排序。

返回这两个区间列表的交集。

（形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b。两个闭区间的交集是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3]。）

输入：A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
注意：输入和所需的输出都是区间对象组成的列表，而不是数组或列表。


链接：https://leetcode-cn.com/problems/interval-list-intersections
"""


def intervalIntersection(A, B):
    """
    区间列表的交集
    思路分析：难点在于寻找最大的开始时间和最小的结束时间，然后遍历
    :param A: 列表1，形式[[]]
    :param B: 列表2，形式[[]]
    :return: 返回交集的list
    算法分析：时间复杂度O(N+M),空间复杂度O(N+M)
    """
    # 先排序
    A.sort()
    B.sort()

    # 定义两个指针
    i, j = 0, 0
    result = []
    while i < len(A) and j < len(B):
        l = max(A[i][0], B[j][0])
        r = min(A[i][1], B[j][1])

        if l <= r:
            result.append([l, r])

        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1
    return result


if __name__ == '__main__':
    print(intervalIntersection(A=[[0, 2], [5, 10], [13, 23], [24, 25]], B=[[1, 5], [8, 12], [15, 24], [25, 26]]))
