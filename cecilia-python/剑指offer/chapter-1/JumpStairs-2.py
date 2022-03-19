#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   JumpStairs-2.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/8 16:08   cecilia      1.0         变态跳台阶（数学规律）
问题描述：
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

"""
'''
其实该问题的实质上考察的是找规律的题型
当n=1时，目前只有一个台阶，此时青蛙只有1种跳法；
当n=2时，有2个台阶，此时青蛙有2种跳法；
当n=3时，有3个台阶，此时青蛙有4种跳法；
当n=4时，有4个台阶，此时青蛙有（1+1+1+1）/（1+2+1）/（2+1+1）/（1+1+2）/（1+3）/（3+1）/（2+2）/（4），总共8种跳法；
以此类推...
当n个台阶时，青蛙有2^(n-1)种跳法
'''
class Solution:
    def jumpStairs(self, n):
        """
        找规律解找跳台阶解法
        :param n:
        :return:
        """
        if n < 3:
            return n
        if n >= 3:
            return 2**(n-1)
