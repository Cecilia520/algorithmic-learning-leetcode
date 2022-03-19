#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   CutRope-1.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/5 15:53   cecilia      1.0         剪绳子
问题描述：
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），每段绳子的长度记为k[0],k[1],...,k[m]。
请问k[0]*k[1]*...*k[m]可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
输入描述:
输入一个数n，意义见题面。（2 <= n <= 60）

示例1
输入：8
输出：18
"""
def cutRope(n):
    """
    剪绳子——贪心法
    根据规律分析：切割越接近自然底数(约等于2.7)乘积越大！
    :param n:
    :return:
    """
    if n == 2:
        return 1
    if n == 3:
        return 2
    x = n % 3
    y = n // 3 # 整除

    if x == 0:
        return int(pow(3, y))
    elif x == 1:
        return 2 * 2 * int(pow(3, y-1))
    else:
        return 2 * int(pow(3, y))

if __name__ == '__main__':
    print(cutRope(n=8))


