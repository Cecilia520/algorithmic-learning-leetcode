#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   2D-arraySearcher.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/27 14:50   cecilia      1.0       针对二维数组的查找
问题描述：
提供一个排好序的二维数组，从左至右递增，从上到下递增，要求给定一个整数，判断该整数是否在二维数组中

问题分析：
1.对于python语言而言，存在一个函数in能够很好地判断元素是否存在数组中；
2.对于算法设计，可以采用二分查找法来进行解决问题
"""


def array2DSearch(nums, target):
    """
    二维数组查找
    方法一：直接遍历法(简单，问题不复杂时，计算时间快)
    :param nums:
    :param target:
    :return:
    """
    flag = 'false'
    for i in range(len(nums)):
        if target in nums[i]:
            flag = 'true'
    return flag


def array2DBinarySearch(nums, target):
    """
    当二维数组每一行的数字都不相等时，直接判断可能存在数组越界等细微问题，此时采用二分查找比较合适
    方法二：二分查找法
    分析：时间复杂度O(nlogn)
    :param nums:
    :param target:
    :return:
    """
    flag = 'false'
    for i in range(len(nums)):
        print("nums[i]:{}".format(nums[i]))
        # 对每一行的数据都使用二分查找
        l, h = 0, len(nums[i]) - 1
        while l <= h:
            mid = int(l + (h - l) / 2)
            print("nums[i][mid]:{}".format(nums[i][mid]))
            if target == nums[i][mid]:
                flag = 'true'
                break
            elif target > nums[i][mid]:
                l = mid + 1  # 如果当前的数据超过了该行的中间数据，那么继续在右区间[mid+1, h]进行查找
            else:
                h = mid - 1 # 小了，往左找
    return flag


if __name__ == '__main__':
    nums = [[1, 2, 3, 4, 5, 6, 7, 8],
            [5, 6, 9, 10, 11, 12, 13, 14]]
    target = 12
    print(array2DSearch(nums, target))
