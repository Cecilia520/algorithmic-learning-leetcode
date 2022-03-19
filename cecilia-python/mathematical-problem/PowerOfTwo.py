#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PowerOfTwo.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/7 21:10   cecilia      1.0         2的次幂
问题描述：
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:

输入: 1
输出: true
解释: 20 = 1
示例 2:

输入: 16
输出: true
解释: 24 = 16
示例 3:

输入: 218
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-two
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def powerOfTwo(num):
    """
    判断是否是2的次幂
    方法一：直接短除法
    :param num:
    :return:
    算法分析：时间复杂度O(logN),空间复杂度O(1)
    """
    if num < 1:
        return False

    while num % 2 == 0:
        num /= 2

    return num == 1


def powerOfTwoPlus(num):
    """
    方法二：位运算：获取二进制中最右边的 1。
    通过x&(-x)保留了数据最右边的1，并将其他的设置为0，如果是2的次幂，那么二进制数中只有一个1，其他的都是0，所以x&(-x)=x。反之，则不符合。
    :param num:
    :return:
    算法分析：时间复杂度O(1)，空间复杂度O(1)
    """
    if num == 0:
        return False
    return num & (-num) == num


if __name__ == '__main__':
    print(powerOfTwoPlus(num=16))
