#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MajorityElement.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/3 19:05   cecilia      1.0       数组中出现次数多于 n / 2 的元素
问题描述：
   给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
   你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
"""
import collections


def majorityElement(nums):
    """
    查找数组中数据重复次数大于2/n的元素
    思路：
      1. 先统计元素的每个元素的重复次数，记录在dict中
      2. 遍历dict，如果次数超过2/n,就输出
    :param nums:
    :return:
    """
    if len(nums) == 0:
        return 0

    dictnums = collections.Counter(nums)

    counts = int(len(nums) / 2)

    for k, v in dictnums.items():
        if v > counts:
            return k


if __name__ == '__main__':
    print(majorityElement(nums=[3, 2, 3]))
