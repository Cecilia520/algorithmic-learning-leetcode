#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   SelectNotes.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/7 16:15   cecilia      1.0        挑选笔记（和打家劫舍题目类似）
薯队长写了n篇笔记，编号从1~n,每篇笔记都获得了不少点赞数。
薯队长想从中选出一些笔记，作一个精选集合。挑选的时候有两个规则：
 1.不能出现连续编号的笔记。
2.总点赞总数最多
如果满足1，2条件有多种方案，挑选笔记总数最少的那种

输入描述:
输入包含两行。第一行整数n表示多少篇笔记。 第二行n个整数分别表示n篇笔记的获得的点赞数。
 （0<n<=1000,    0<=点赞数<=1000)

输出描述:
输出两个整数x,y。空格分割。
 x表示总点赞数，y表示挑选的笔记总数。

输入例子1:
4
1 2 3 1

输出例子1:
4 2

"""
'''
该道题主要是考察动态规划类型的题目，类似打家劫舍的问题
可以定义dp[i]数组表示挑选第i个笔记的时最大总点赞数；
dpcount[i]表示挑选第i个笔记时笔记的总数
如果当前的第i个笔记没有被挑选：
    dp[i] = dp[i+2] + nums[i]
    dpcount[i] = dpcount[i+2] + 1
如果当前第i个笔记被挑选了，：
    dp[i] = dp[i+1]
    dpcount[i] = dpcount[i+1]
'''
N = int(input().strip())
note_list = list(map(int, input().strip().split()))
dp = [0 for _ in range(N + 2)]
dpcount = [0 for _ in range(N + 2)]
for i in range(N - 1, -1, -1):
    if dp[i + 1] < dp[i + 2] + note_list[i]:
        dp[i] = dp[i + 2] + note_list[i]
        dpcount[i] = dpcount[i + 2] + 1
    else:
        dp[i] = dp[i + 1]
        dpcount[i] = dpcount[i + 1]
print(dp[0], dpcount[0])
