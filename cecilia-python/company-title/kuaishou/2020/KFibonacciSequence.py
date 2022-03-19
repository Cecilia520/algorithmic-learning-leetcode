#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   KFibonacciSequence.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/19 21:37   cecilia      1.0       K阶斐波那契数列
问题描述：
给定常数K，数列的定义如下：
a[1] =1,若i=0，1，2，...K-1
a[i]=a[i-1]+a[i-2]+a[i-3]+...+a[i-K],若i>=K
现在要求a[n]%397(a[n]除以397的余数)的值

输入描述：两个正整数K和N
输出结果

示例：
输入：
2 4

输出：
5

解释：数列为：1 1 2 3 5 8 13 21 34 ........刚好为二阶斐波那契数列
"""
# 数列正好符合类似的斐波那契的数列的规律
import sys

while True:
    try:
        k, n = map(int, sys.stdin.readline().strip().split())
        if n <= k - 1 and n >= 0:
            print(1)
            exit(0)
        if n >= k:
            # 定义状态
            dp = [0] * (n + 1)
            # 初始化
            for i in range(0, k):
                dp[i] = 1
            for j in range(k, n + 1):
                index = k
                while index > 0:
                    dp[j] += dp[j - index]
                    index -= 1
        print(dp[n])
        exit(0)
    except:
        break

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    for i in range(5, 3, -1):
        print(i)
