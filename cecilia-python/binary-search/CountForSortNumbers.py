#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   CountForSortNumbers.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/9 21:24   cecilia      1.0        统计一个有序数组中数字出现的次数
问题描述：
给定一个有序整数数组，统计其出现的次数
"""


def GetNumberOfK(data, k):
    """
    统计指定的数字在有序数组中出现的次数
    :param data:
    :param k:
    :return:
    """
    return getUpper(data, k) - getLower(data, k) + 1


def getUpper(data, k):
    """
    二分查找出现的高位
    :param data:
    :param k:
    :return:
    """
    start, end = 0, len(data) - 1
    while start <= end:
        mid = int(start + (end - start) / 2)
        if data[mid] <= k:
            start = mid + 1
        else:
            end = mid - 1
    return end


def getLower(data, k):
    """
    二分查找出现的低位
    :param data:
    :param k:
    :return:
    """
    start, end = 0, len(data) - 1
    while start <= end:
        mid = int(start + (end - start) / 2)
        if data[mid] < k:
            start = mid + 1
        else:
            end = mid - 1
    return start


if __name__ == '__main__':
    print(GetNumberOfK(data=[1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9, 10, 10, 10, 10, 11], k=10))
