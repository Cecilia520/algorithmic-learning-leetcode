#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   FindNumsAppearOnce.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/17 22:08   cecilia      1.0       在数组中找出只出现一次的两个数
问题描述：
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
思路一：采用递归判断，根据中间的数将其分成两个小数组，每次递归下去，如果出现最后两个数据不相等，那么即是我们需要的数据
思路二：位运算。两个相同数字异或等于0，一个数和0异或还是它本身。
注：因为内存的限制，不能使用字典存储次数
"""
def findNumsAppearOnce(arr):
    """
    思路一：递归
    :param arr:
    :return:
    """
    def divideMerge(arr, start, end):
        """
        将一个数组分成多个小数组，逐一判断
        :param arr:
        :param start:
        :param end:
        :return:
        """
        res = set()
        if start > end:
            return res
        if start == end:
            return set(arr[start:end+1])

        mid = start + int((end - start)/2)
        res1 = divideMerge(arr, start, mid)
        res2 = divideMerge(arr, mid+1,end)
        return res1.union(res2).difference(res1.intersection(res2))

    return divideMerge(arr, 0, len(arr)-1)
