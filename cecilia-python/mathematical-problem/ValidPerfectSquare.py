#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ValidPerfectSquare.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/3 19:06   cecilia      1.0         平方数
问题描述：
   给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt。

示例 1：

输入：16
输出：True
示例 2：

输入：14
输出：False

算法思路：二分查找和牛顿法迭代
"""
def validPerfectSquare(num):
    """
    二分查找法：
       1. 定区间[2, num/2]，计算mid=int(left+(right-left)/2)
       2. 如果mid * mid < num,则mid = left + 1;
       3. 如果mid * mid == num,则返回True；
       4. 否则right-1
    :param num:
    :return:
    算法分析：时间复杂度O(logN),空间复杂度O(1)
    """
    if num < 2:
        return True

    left, right = 2, num/2
    while left <= right:
        mid = int(left+(right-left)/2)
        if mid * mid == num:
            return True
        elif mid * mid < num:
            left = mid + 1
        else:
            right = mid - 1
    return False

def validPerfectSquare2(num):
    """
    牛顿法：利用2/num作为初始值，然后使用牛顿法求取下一个近似值x(K+1) = 1/2(x(K) + num/x(k))
    :param num:
    :return:
    算法分析：时间复杂度O(logN),空间复杂度O(1)
    """
    if num < 2:
        return True

    x = num // 2
    while x * x > num:
        x = (x/num + x) // 2

    return x * x == num

if __name__ == '__main__':
    print(validPerfectSquare(num=16))
