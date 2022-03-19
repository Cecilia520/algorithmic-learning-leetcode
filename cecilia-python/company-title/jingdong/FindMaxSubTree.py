#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   FindMaxSubTree.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/17 22:10   cecilia      1.0        寻找最短疏散时间
问题描述：体育场突然着火了，现场需要紧急疏散，但是过道真的是太窄了，同时只能容许一个人通过。
现在知道了体育场的所有座位分布，座位分布图是一棵树，已知每个座位上都坐了一个人，安全出口在树的根部，也就是1号结点的位置上。
其他节点上的人每秒都能向树根部前进一个结点，但是除了安全出口以外，没有任何一个结点可以同时容纳两个及以上的人，这就需要一种策略，
来使得人群尽快疏散，问在采取最优策略的情况下，体育场最快可以在多长时间内疏散完成。

问题考查：实际上考察的是每个子树的最大节点数
方法：双向队列或者并查集

并查集定义：一种树型的数据结构，用于处理一些不相交集合（Disjoint Sets）的合并及查询问题。常常在使用中以森林来表示。
"""
import sys


class UF:
    """
    创建一个并查集数据结构，用于存储每个集合以及每个集合的最大个数
    """

    def __init__(self, cnt):
        self.parent = {}
        self.cnt = cnt  # 用于统计记录每个子树的节点数

    def find(self, x):
        """
        查询元素
        :param x:
        :return:
        """
        self.parent.setdefault(x, x)
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, p, q):
        """
        合并两个子集
        :param p:
        :param q:
        :return:
        """
        self.parent[self.find(p)] = self.find(q)


class Solution:
    def findMinTimeForTree(self, matrix, n):
        """
        计算最短疏散时间，转化成找每个子树的最大节点数
        :param matrix:树对应的邻接矩阵
        :param n 树的节点数目
        :return:
        """

        visit = [0] * n  # 记录每个节点是否被访问的数组
        max_time = 0
        visit[0] = 1

        for u in matrix[0]:
            visit[u] = 1
            queue = [u]
            tmp = 0
            while len(queue) != 0:
                tmp += 1
                v = queue.pop()
                for i in matrix[v]:
                    if visit[i] == 0:
                        visit[i] = 1
                        queue.append(i)
            max_time = max(tmp, max_time)
        return max_time

    def findMinTimeForTreeByUF(self, matrix, n):
        """
        使用并查集解决问题
        :param matrix:
        :param n:
        :return:
        算法分析：时间复杂度O(n),空间复杂度O（n）
        """
        pass


if __name__ == '__main__':
    s = Solution()
    n = int(sys.stdin.readline().strip())
    matrix = {}
    for i in range(n):
        matrix[i] = []

    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().strip().split(' '))
        matrix[u - 1].append(v - 1)
        matrix[v - 1].append(u - 1)

    ans = s.findMinTimeForTree(matrix, n)
    print(ans)
