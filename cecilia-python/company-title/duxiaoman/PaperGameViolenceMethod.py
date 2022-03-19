#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PaperGame.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/20 20:55   cecilia      1.0         撕纸片游戏（考察博弈论）——暴力法
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
from typing import List


def cut_to_one(paper_collection: List[List[int]]):
    """
    将纸片剪成[1,1]的纸片
    :param paper_collection: 纸片集合
    :return: 是否可以将纸片剪成[1,1]的纸片, 如果可以则剪纸并返回 True, 如果不可以返回 False
    """
    if len(paper_collection) == 1 and paper_collection[0][0] == paper_collection[0][1] == 1:
        return True
    for paper in paper_collection:
        if paper[0] == 1 or paper[1] == 0:
            paper_collection.remove(paper)
            paper_collection.append([1, 1])
            if paper[0] == 1:
                paper_collection.append([1, paper[1] - 1])
            else:
                paper_collection.append([paper[0] - 1, 1])
            return True
    return False


def cut_to_two(paper_collection: List[List[int]]):
    """
    将纸片剪成[x>=2, y>=2] 的纸片
    :param paper_collection: 纸片集合
    :return: 是否可以将纸片剪成边长大于等于2的纸片, 如果可以则剪纸并返回 True, 如果不可以返回 False
    """
    for paper in paper_collection:
        if paper[0] >= 4 and paper[1] >= 2:
            paper_collection.append([2, paper[1]])
            paper_collection.append([paper[0] - 2, paper[1]])
            paper_collection.remove(paper)
            return False
        elif paper[0] >= 2 and paper[1] >= 4:
            paper_collection.append([paper[0], 2])
            paper_collection.append([paper[0], paper[1] - 2])
            paper_collection.remove(paper)
            return False
    return True


def check(paper_collection: List[List[int]]):
    """
    检查集合中是否有[1,1]的元素
    :param paper_collection: 纸片集合
    :return: 集合中是否有[1,1]的元素
    """
    for paper in paper_collection:
        if paper[0] == 1 and paper[1] == 1:
            return True
    return False


def judge(x: int, y: int):
    """
    判断剪切纸片为[1,1]我是否会赢
    :param x: 长
    :param y: 宽
    :return: 我是否会赢
    """
    paper_collection = [[x, y]]
    my_turn = True
    lose = False
    while True:
        if not cut_to_one(paper_collection):
            lose = cut_to_two(paper_collection)
        if lose or check(paper_collection):
            break
        else:
            my_turn = False if my_turn else True

    if (my_turn and not lose) or (not my_turn and lose):
        return True
    else:
        return False


if __name__ == '__main__':
    """
    测试数据
    4 2 WIN
    3 2 LOSE
    2 2 LOSE
    """
    cnt = 0
    while True:
        array_str = input("In[{}]: ".format(cnt))
        cnt = cnt + 1
        if "-1" == array_str:
            break
        array = list(map(int, array_str.split(" ")))
        if judge(array[0], array[1]):
            print("WIN")
        else:
            print("LOSE")
