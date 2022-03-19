#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   CutRope-1.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/8 16:06   cecilia      1.0        剪绳子-1(先数学推导，再实现)
问题描述：
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1，m<=n），
每段绳子的长度记为k[1],...,k[m]。请问k[1]x...xk[m]可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例1:

输入
8
输出
18
"""
'''
解题思路：该题目的问题实质就是给定一个整数n，如何将其划分成m个数，并且这m个数的和为n，乘积最大的一个组合
首先根据数学推导计算出：数学推导总体分为两步：① 当所有绳段长度相等时，乘积最大。② 最优的绳段长度为 3 。
设将绳子按照 x 长度等分为 a 段，即 n = ax ，则乘积为 x^a。观察以下公式，由于 n 为常数，因此当 x^((1/x)*n)取最大值时， 乘积达到最大值。
设定y=x^(1/x)，经过求导可以知道当x=e时值比较大，最终确定为a=3
因此：
当n<=3时，按照规则应不切分，至少m>1,即返回n-1；
当n>3时，分成以下情况，求n除以3的整数部分a和余数部分b，即n=3a+b：
- 当b=0时，直接返回3^a;
- 当b=1时，由于1+3需要换成2+2，因此3^(a-1)*4;
- 当b=2时，返回3^a*2
'''


class Solution:
    def CutRope(self, n, m):
        """
        计算剪绳子为m段后最大乘积
        :param n: 总长度
        :param m: 段数
        :return:
        """
        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return 3 ** a
        elif b == 1:
            return 3 ** (a-1) * 4 # 需要将1+3换成2+2
        elif b == 2:
            return 3 ** a * 2

if __name__ == '__main__':
    s =Solution()
    print(s.CutRope(n=8, m=3))
