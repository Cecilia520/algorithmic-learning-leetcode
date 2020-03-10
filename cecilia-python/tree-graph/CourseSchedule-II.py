#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   CourseSchedule-II.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/9 22:08   cecilia      1.0         课程表安排的合理
问题描述：
现在你总共有 n 门课需要选，记为 0 到 n-1。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。

可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。

示例 1:

输入: 2, [[1,0]]
输出: [0,1]
解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
示例 2:

输入: 4, [[1,0],[2,0],[3,1],[3,2]]
输出: [0,1,2,3] or [0,2,1,3]
解释: 总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
     因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。

思路：
利用结点的入度为0，可以以任何的顺序进行拓扑排序
算法过程：
  1. 初始化一个队列，用于存储每个入度为0的结点；
  2. 用数组记录每一个结点的入度数
  3. 用邻接矩阵记录每个节点的邻接结点
  4. 遍历所有课程，如果当前结点的入度为0，则入队；
      如果当前的队列不为空，那么弹出一个元素N；
      对N的所有邻接结点的入度尽心减1，如果入度为0时，将其加入队列中；
  5. 将节点加入拓扑排序列表中
"""
from collections import defaultdict


def getCourseSchedule(numCourses, prerequisites):
    """
    获取最合理的课程顺序
    :param numCourses:
    :param prerequisites:
    :return:
    """
    # 初始化邻接矩阵
    adj_list = defaultdict(list)
    # 入度字典
    indegree = {}
    # 获取所有课程的入度数以及邻接矩阵
    for dest, src in prerequisites:
        adj_list[src].append(dest)
        indegree[dest] = indegree.get(dest, 0) + 1

    # 如果当前的入度为0，则入度
    zero_indegree_queue = [k for k in range(numCourses) if k not in indegree]

    result = []

    # Until there are nodes in the Q
    while zero_indegree_queue:

        # 弹出入度为0的结点
        vertex = zero_indegree_queue.pop(0)
        result.append(vertex)

        # 如果当前结点在邻接矩阵中
        if vertex in adj_list:
            for neior in adj_list[vertex]:
                indegree[neior] -= 1  # 在，就入度减1

                # 如果当前入度减为0，那么加入队列
                if indegree[neior] == 0:
                    zero_indegree_queue.append(neior)

    return result if len(result) == numCourses else []


if __name__ == '__main__':
    print(getCourseSchedule(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]))
