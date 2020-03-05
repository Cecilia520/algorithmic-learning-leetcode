#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   IntConvertToBase7.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/3 18:56   cecilia      1.0         7进制转换
问题描述：
给定一个整数，将其转化为7进制，并以字符串形式输出。

输入: 100
输出: "202"
示例 2:

输入: -7
输出: "-10"
注意: 输入范围是 [-1e7, 1e7] 。
"""


def intConvertToBase7(num) -> str:
    """
    将一个整数转化成字符串
    算法思路：短除法
    :param num:
    :return:
    """
    base7 = []
    # 如果当前的数是负数，则添加负号
    if num < 0:
        flag = 1
        num = -num
    else:
        flag = 0
    # 短除法
    while num >= 7:
        fig = str(num % 7)
        base7.append(fig)
        num = num // 7
    base7.append(str(num))

    if flag:
        base7.append('-')
    base7.reverse()

    return ''.join(base7)

if __name__ == '__main__':
    print(intConvertToBase7(num=100))
