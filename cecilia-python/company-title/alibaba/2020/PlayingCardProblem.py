#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PlayingCardProblem.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/30 22:06   cecilia      1.0       扑克牌问题
问题描述：
今天小强从一副扑克牌（总共40张，有10种）中拿出一叠，其中包括A,2,3,4...10各四张，其中A代表1。
他从这一叠中抽出一些牌给小明，并告诉小明每次可以按照下列方式打出一些牌：
    单牌：一张牌，例如3.
    对子：数字相同的两张牌，例如44；
    顺子：数字连续的五张牌，例如A2345；
    连对：数字连续的三个对子，例如334455。
    现在小强想知道最少打出多少次牌可以打光手中的牌。

> 输入描述：一行十个空格分隔的整数A1，A2，A3，A4......A10，分别代表为A,2,3,4...10总共10种牌的个数。
> 例如：Input: 1 1 1 2 2 2 2 2 1 1
> OutPut: 3
> 输出描述：连续打出三个顺子，分别是A2345，45678，678910。可以最少打完手中的牌

"""
