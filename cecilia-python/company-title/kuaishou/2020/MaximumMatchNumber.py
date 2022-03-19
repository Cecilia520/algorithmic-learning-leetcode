#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MaximumMatchNumber.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/19 21:31   cecilia      1.0        最大火柴数字
问题描述：用火柴组合成一串数字，挪动一根火柴，使得挪动后地数字最大，相信这个游戏大家都玩过，请写一个程序实现这个功能。
如果移动任意一根火柴会导致无法组成一个新的数字，输出-1，0~9用火柴棍拼接方法如下：
0123456789

输入数字N，（0<=N<=100000000）

输出描述：输出结果M

示例：
输入：109
输出：705
"""
import sys

change_self = ['0', '6', '3', '2']
change_by_other = ['1', '3', '5', '6', '1']
be_change = ['9', '7', '8']

def do_change_self(s: str):
    if s == '0' or s == '6':
        return '9'
    elif s == '2':
        return '3'
    elif s == '3':
        return '5'


def can_be_changed(s: str):
    for i in range(len(s) - 1, -1, -1):
        if s[i] in be_change:
            return True, s[:i] + do_be_changed(s[i] + s[i + 1:])


def do_be_changed(s: str):
    if s == '9':
        return '5'
    elif s == '7':
        return '1'
    elif s == '8':
        return '0'


def do_change_by_other(s: str):
    if s == '1':
        return '7'
    elif s == '3':
        return '9'
    elif s == '6':
        return '8'
    elif s == '1':
        return '7'

def change(m: int):
    match_str = str(m)
    for i in range(len(match_str)):
        if match_str[i] in change_self:
            return int(match_str[:i]) + do_change_self(match_str[i]) + match_str[i + 1:]
        if match_str[i] in change_by_other:
            changed, changed_str = can_be_changed(match_str[i + 1:])
            if changed:
                return int(match_str[:i] + do_change_by_other(match_str[i]) + changed_str)

while True:
    try:
        N = int(sys.stdin.readline().strip())
        M = change(N)
        print(M)
        exit(0)
    except:
        break