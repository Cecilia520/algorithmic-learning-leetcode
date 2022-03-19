#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   CourseSchedule.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/9 22:04   cecilia      1.0         None
问题描述：
现在你总共有 n 门课需要选，记为 0 到 n-1。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

给定课程总量以及它们的先决条件，判断是否可能完成所有课程的学习？

示例 1:

输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
说明:

输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
提示:

这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
通过 DFS 进行拓扑排序 - 一个关于Coursera的精彩视频教程（21分钟），介绍拓扑排序的基本概念。
拓扑排序也可以通过 BFS 完成。

思路分析：课程安排图是否是 有向无环图(DAG)。即课程间规定了前置条件，但不能构成任何环路，否则课程前置条件将不成立。

"""


def isCourseSchedule(numCourses, prerequisites) -> bool:
    """
    判断当前课程安排的的是否合理
    思路：题目的实质就是判断该课程安排图是否是有向无环图（深度优先遍历或者广度优先遍历、拓扑排序）
    :param numCourses: 总的课程数
    :param prerequisites: 课程图
    :return:
    算法分析：
    """
    indegrees = [0 for _ in range(numCourses)]  # 入度表，用于记录课程安排表中每一个结点的入度数
    adjacency = [[] for _ in range(numCourses)]  # 邻接矩阵，用于记录每个节点的前驱结点的邻接结点

    queue = []  # 用于存储入度为0的结点

    # 获取每门课程的入度和邻接点
    for pre, curr in prerequisites:
        indegrees[curr] += 1
        adjacency[pre].append(curr)

    # 获取所有课程入度为0的结点
    for i in range(len(indegrees)):
        # 如果当前的结点不在入度表中，加入即可
        if not indegrees[i]:
            queue.append(i)

    # BFS 拓扑排序
    while queue:
        pre = queue.pop(0)
        numCourses -= 1
        # 若当前结点的前驱结点在邻接矩阵中，那么表示存在环
        for curr in adjacency[pre]:
            indegrees[curr] -= 1  # 入度减1
            # 如果当前结点没有入度，添加即可
            if not indegrees[curr]:
                queue.append(curr)
    return not numCourses  # 如果最后课程数为0，那么说明该图不存在环，安排的合理


if __name__ == '__main__':
    print(isCourseSchedule(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]))
