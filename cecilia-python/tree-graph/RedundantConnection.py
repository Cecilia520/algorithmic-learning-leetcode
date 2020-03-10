#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   RedundantConnection.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/9 22:09   cecilia      1.0         并查集
问题描述：
在本问题中, 树指的是一个连通且无环的无向图。

输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。

结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v] ，满足 u < v，表示连接顶点u 和v的无向图的边。

返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。答案边 [u, v] 应满足相同的格式 u < v。

示例 1：

输入: [[1,2], [1,3], [2,3]]
输出: [2,3]
解释: 给定的无向图为:
  1
 / \
2 - 3
示例 2：

输入: [[1,2], [2,3], [3,4], [1,4], [1,5]]
输出: [1,4]
解释: 给定的无向图为:
5 - 1 - 2
    |   |
    4 - 3
注意:

输入的二维数组大小在 3 到 1000。
二维数组中的整数在1到N之间，其中N是输入数组的大小。

思路：
方法一：DFS
对于每个边 (u, v)，用深度优先搜索遍历图，以查看是否可以将 u 连接到 v。如果可以，则它是重复边。
算法分析：
时间复杂度：O(N^2)。其中 NN 是图中的结点数（以及边数）。在最坏的情况下，对于我们包含的每一条边，我们必须搜索图中出现的每一条边。
空间复杂度：O(N)，图的当前构造最多有 N个结点。

方法二：并查集
一个 DSU 数据结构可以用来维护图形连接组件的数据，并快速查询它们。有两种操作：

dsu.find(node x)，找到元素 x 所在的集合的代表，该操作也可以用于判断两个元素是否位于同一个集合。
dsu.union(node x, node y)，把元素 x 和元素 y 所在的集合合并，要求 x和 y 所在的集合不相交，如果相交则不合并。

"""
from typing import List


class disjoint():
    def __init__(self, N):
        """
        初始化
        :param N:
        """
        self.array = [-1] * N

    def find(self, i):
        """
        寻找元素i所在的集合代表，该操作用于判断两个元素是否位于同一个集合
        :param i:
        :return:
        """
        while self.array[i] != -1:
            i = self.array[i]
        return i

    def union(self, i, j):
        """
        合并i和j元素，要求i和j所在集合不相交，如果相交则不合并
        :param i:
        :param j:
        :return:
        """
        # 分别找到各自的所在集合的代表
        i = self.find(i)
        j = self.find(j)

        if (i != j) or (i == -1 and j == -1):
            self.array[i] = j
            return j
        else:
            return -1


class Solution():
    def redundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        冗余连接
        :param edges:
        :return:
        """
        a = set()
        for i in edges:
            a.add(i[0])
            a.add(i[1])

        # 构建树
        tree = disjoint(len(a) + 1)

        answer = []
        for i in edges:
            # 找到每个元素的代表集
            x, y = tree.find(i[0]), tree.find(i[1])
            if (x != y) or (x == -1 and y == -1):
                tree.union(i[0], i[1])
            else:
                answer = i
        return answer


if __name__ == '__main__':
    s = Solution()
    print(s.redundantConnection(edges=[[1, 2], [1, 3], [2, 3]]))
