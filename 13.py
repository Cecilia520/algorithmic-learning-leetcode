#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   13.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/9/17 20:15   cecilia      1.0         None
在某网络游戏中提供了一个道具库，在道具库中每种道具均有若干件（数量已知），游戏玩家购买一件道具将获得一定的魅力值。

已知每种道具的价格和魅力值，请编写一个程序，在总价格不超过某个上限的情况下使得所购道具的魅力值之和达到最大。

输入描述
单组输入。

每组测试数据的输入有n+1行，n表示道具的种类。

第1行包含两个正整数，分别表示道具种类数n和总价值的上限p，两个数字之间用空格隔开。 （n<=100，p<=10000）

第2行到第n+1行分别对应于第1种道具到第n种道具的信息，每1行包含三个正整数，两个数字之间用空格隔开，三个正整数分别表示某一种道具的数量、单个道具的价格和魅力值。

输出描述
每组测试数据的输出只有一行，即道具魅力值的最大和。


样例输入
3 10
2 2 3
1 5 10
2 4 12
样例输出
27
"""
class Solution:
    def getMaxValue(self, matrix, n, p)->int:
        """
        计算最大道具的魅力值
        :param matrix:
        :param n:
        :param p: 总价值上限
        :return:
        """
        dp = [0 for _ in range(p+1)]

        for i in range(n):
            for j in range(p, -1, -1):
                k = min(j // matrix[i][1], matrix[i][0])
                dp[j] = max([dp[j - x * matrix[i][1]] + x * matrix[i][2] for x in range(k+1)])
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    n, p = map(int, input().strip().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().strip().split())))
    print(s.getMaxValue(matrix, n, p))

