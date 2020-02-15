#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   FirstBadVersion.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/15 13:32   cecilia      1.0       找出第一个版本出现错的版本
问题描述：
你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

示例：
给定 n = 5，并且 version = 4 是第一个错误的版本。
调用 isBadVersion(3) -> false
调用 isBadVersion(5) -> true
调用 isBadVersion(4) -> true
所以，4 是第一个错误的版本。 

问题分析：
区间范围是[1,n],如果第 m 个版本出错，则表示第一个错误的版本在 [l, m] 之间，令 h = m；否则第一个错误的版本在 [m + 1, h] 之间，令 l = m + 1。
第一个错误版本，即是寻找最左端最小的元素！
"""


def isBadVersion():
    """
    检查当前版本是否是错误版本
    :param n:
    :return:
    """
    return False


def firstBadVersion(n) -> int:
    """
    :param n:
    :return:
    """
    l, h = 1, n
    while l < n:
        mid = l + (h - l) / 2
        if isBadVersion(mid):
            h = mid
        else:
            l = mid + 1
    return h
