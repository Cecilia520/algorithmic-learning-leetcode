#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   HasPathForMatrix.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/3 16:22   cecilia      1.0        矩阵中的路径问题
问题描述：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 例如 [[a b c e]
                                                         [s f c s]
                                                         [a d e e]]
矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。

思路分析：典型的回溯法问题。
1.初始化一个标识路径是否走过的数组，大小和matrix相等，走过了，标识为True，没有做过的表示为False；
2.根据行数和列数遍历，找到str中和matrix中匹配的的第一个元素，然后进入回溯递归分别向向左、向右、向上、向下四个方位进行寻找，如果有，则标识为True；
3.根据i和j先确定一维数组的位置，因为给定的matrix是一个一维数组，如果是二维数组，可以分开遍历；
4.确定回溯终止条件：i和j索引越界，超过了数组长度，或者标识索引位置对应为True或者path路径数组中该索引位置的元素和matrix不相等；
5.如果start索引运行到path路径数组的最后位置，那么返回True，说明全部找到了；
6.遍历每一个元素的时候都需要进入回溯中进行判断周围是否存在可达的路径，如果最后都找不到，还原flag数组中的标识为False，继续寻找其他的路径
"""


def hasPathForMatrix(matrix, rows, cols, path):
    """
    判断矩阵中是否存在指定字符串的可达路径
    :param matrix: 给定的矩阵
    :param rows: 行数
    :param cols: 列数
    :param path: 指定的字符串
    :return:
    """

    def backtrack(matrix, i, j, rows, cols, flag, path, start):
        """
        针对每一个元素的回溯
        :param matrix: 给定的矩阵
        :param i: 索引元素的行i
        :param j: 索引元素的列j
        :param rows: 总行数
        :param cols: 总列数
        :param flag: 标识数组
        :param path: 指定的字符串
        :param start: 字符串数组的开始索引，初始值为0
        :return:
        """
        # 计算每个元素在数组中的位置索引
        index = i * cols + j

        # 确定终止条件
        if i < 0 or j < 0 or i >= rows or j >= cols or matrix[index] != path[index] or flag[index]:
            return False
        # 如果start走到字符串数组的末尾，那么直接返回True
        if start == len(path):
            return True

        # 回溯部分,分别向左、右、上、下四个方位开始搜索
        if backtrack(matrix, i - 1, j, rows, cols, flag, start + 1) or backtrack(matrix, i + 1, j, rows, cols, flag, start + 1) or backtrack(matrix, i, j - 1, rows, cols, flag, start + 1) or backtrack(matrix, i, j + 1, rows, cols, flag, start + 1):
            return True

        # 如果没找到，还原标识，继续寻找其他的
        flag[index] = False
        return False

    # 创建标识数组，并初始化为false，表示都没有走过
    flag = [False for _ in range(len(matrix))]
    for i in range(rows):
        for j in range(cols):
            if backtrack(matrix, i, j, rows, cols, flag, path, 0):
                return True
    return False
