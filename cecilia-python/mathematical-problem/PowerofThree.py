#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PowerofThree.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/3 19:07   cecilia      1.0         3的次方
问题描述：
 给定一个整数，写一个函数来判断它是否是 3 的幂次方。

示例 1:

输入: 27
输出: true
示例 2:

输入: 0
输出: false
示例 3:

输入: 9
输出: true
示例 4:

输入: 45
输出: false

>> 进阶：
  你能不使用循环或者递归来完成本题吗？


"""
def powerofThree(num):
    """
    直接循环迭代判断是否被3整除多次后的余数位0，商位1
    :param num:
    :return:
    """
    if num < 1:
        return False

    while num % 3 == 0:
        num /= 3

    return num == 1

if __name__ == '__main__':
    print(powerofThree(num=9))
