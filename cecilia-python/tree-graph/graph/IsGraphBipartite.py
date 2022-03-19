#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   IsGraphBipartite.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/9 22:03   cecilia      1.0         是否是二分图
问题描述：
给定一个无向图graph，当这个图为二分图时返回true。

如果我们能将一个图的节点集合分割成两个独立的子集A和B，并使图中的每一条边的两个节点一个来自A集合，一个来自B集合，我们就将这个图称为二分图。

graph将会以邻接表方式给出，graph[i]表示图中与节点i相连的所有节点。每个节点都是一个在0到graph.length-1之间的整数。这图中没有自环和平行边： graph[i] 中不存在i，并且graph[i]中没有重复的值。


示例 1:
输入: [[1,3], [0,2], [1,3], [0,2]]
输出: true
解释:
无向图如下:
0----1
|    |
|    |
3----2
我们可以将节点分成两组: {0, 2} 和 {1, 3}。

示例 2:
输入: [[1,2,3], [0,2], [0,1,3], [0,2]]
输出: false
解释:
无向图如下:
0----1
| \  |
|  \ |
3----2
我们不能将节点分割成两个独立的子集。
注意:

graph 的长度范围为 [1, 100]。
graph[i] 中的元素的范围为 [0, graph.length - 1]。
graph[i] 不会包含 i 或者有重复的值。
图是无向的: 如果j 在 graph[i]里边, 那么 i 也会在 graph[j]里边。

算法分析：
1. 使用颜色数组记录每一个结点的颜色，颜色可以是0，1，也可以是未着色null或者-1；
2. 贪心思想给图着色。搜索节点时，需要考虑图是非连通的情况。对每个未着色节点，从该节点开始深度优先搜索着色。每个邻接点都可以通过当前节点着相反的颜色。如果存在当前点和邻接点颜色相同，则着色失败。
3.使用栈完成深度优先搜索，存储着下一个要访问节点的顺序。在 graph[node] 中，对每个未着色邻接点，着色该节点并将其放入到栈中。
"""


def isBipartite(graph):
    """
    判断是否是二分图
    方法：深度优先遍历+贪心思想
    :param graph:
    :return:
    算法分析：时间复杂度O(N+E),空间复杂度O(N)
    """
    colors = {}  # 用来记录每个节点的颜色
    for node in range(len(graph)):
        if node not in colors:
            stack = [node]
            colors[node] = 0
        while stack:
            node = stack.pop()
            for curr in graph[node]:
                if curr not in colors:
                    stack.append(curr)
                    colors[curr] = colors[node] ^ 1  # 颜色改变成1
                elif colors[curr] == colors[node]:
                    return False
    return True


if __name__ == '__main__':
    print(isBipartite(graph=[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
