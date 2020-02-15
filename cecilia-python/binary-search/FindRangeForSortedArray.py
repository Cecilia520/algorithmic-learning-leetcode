#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   FindRangeForSortedArray.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/15 13:34   cecilia      1.0        为一个有序数组寻找区间[start,end]

问题描述：
给定一个有序数组 nums 和一个目标 target，要求找到 target 在 nums 中的第一个位置和最后一个位置。

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


def findfirst(nums, target):
    """
    在有序数组中寻找出现的第一个目标元素
    :param nums:
    :param target:
    :return:
    注意：在寻找第一个位置的二分查找代码中，需要注意 h 的取值为 nums.length，而不是 nums.length - 1。先看以下示例：
        nums = [2,2], target = 2
    如果 h 的取值为 nums.length - 1，那么 last = findFirst(nums, target + 1) - 1 = 1 - 1 = 0。
    这是因为 findLeft 只会返回 [0, nums.length - 1] 范围的值，对于 findFirst([2,2], 3) ，
    我们希望返回 3 插入 nums 中的位置，也就是数组最后一个位置再往后一个位置，
    即 nums.length。所以我们需要将 h 取值为 nums.length，从而使得 findFirst返回的区间更大，
    能够覆盖 target 大于 nums 最后一个元素的情况。
    """
    l, h = 0, len(nums)
    while l < h:
        mid = int(l + (h - l) / 2)
        if nums[mid] >= target:
            h = mid
        else:
            l = mid + 1
    return l


def findRangeForSortedArray(nums, target):
    """
    根据一个有序数组寻找目标值的所在区间
    :param nums:
    :param target:
    :return:
    """
    # 用二分查找找出第一个位置和最后一个位置，但是寻找的方法有所不同，需要实现两个二分查找。
    # 可以将寻找 target 最后一个位置，转换成寻找 target+1 第一个位置，再往前移动一个位置
    start = findfirst(nums, target)
    end = findfirst(nums, target + 1) - 1

    if start == len(nums) or nums[start] != target:
        return [-1, -1]
    else:
        return [start, max(start, end)]


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(findRangeForSortedArray(nums, target))
