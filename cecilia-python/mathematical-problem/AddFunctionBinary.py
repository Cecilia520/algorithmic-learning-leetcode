#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   AddFunctionBinary.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/3 19:03   cecilia      1.0        二进制加法运算
问题描述：给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"

"""


def addFunctionBinary(a, b):
    """
    二进制加法运算
    方法一：位运算
       1. 把a和b转化成整型数据x和y，x保存结果，y保存进位；
       2. 当y不进位时：
          a. 计算无进位加法结果：x^y;
          b. 计算当前的进位：carry=(x & y) << 1;
          c. 更新x=answer,y=carry
    :param a:
    :param b:
    :return:
    """
    x, y = int(a, 2), int(b, 2)

    while y:
        answer = x ^ y # XOR异或运算 3 ^ 1 =
        carry = (x & y) << 1 #位运算
        x = answer
        y = carry
    return bin(x)[2:] # 返回二进制整数


if __name__ == '__main__':
    print(addFunctionBinary(a="11", b="1"))
