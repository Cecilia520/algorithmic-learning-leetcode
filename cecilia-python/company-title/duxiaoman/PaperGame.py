#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PaperGame.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/20 20:55   cecilia      1.0         撕纸片游戏（考察博弈论）
问题描述：
A和B正在博弈，他们的博弈道具是一张初始为n*m的纸片。
每次操作，都可以把一张x*y的纸片剪成x*t和x*(y-t)（t>=1,y-t>=1）的两张纸片；
也可以分成y*t和y*(x-t)（t>=1,x-t>=1）的两张纸片（x和y均为正整数），纸片一分为二，可以选取任意一个部分进行后续操作，最终先切出1*1
的人获胜。
现在你是A，你想知道在自己先手的情况下，俩人都是足够聪明的情况下谁会赢？如果你会赢，输出为WIN，否则输出LOSE

输入描述：输入每组数据两个整数，代表一开始的纸片n*m，2<=n<=200,2<=m<=200
输出描述：胜利输出WIN，否则输出LOSE

示例：
输入：
4 2
3 2
2 2

输出：
WIN
LOSE
LOSE
"""
