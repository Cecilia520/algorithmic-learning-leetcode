#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MinimumMovesToEqualArrayElementsII.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/3 19:05   cecilia      1.0         相遇问题
问题描述：
给定一个非空整数数组，找到使所有数组元素相等所需的最小移动数，
    其中每次移动可将选定的一个元素加1或减1。 您可以假设数组的长度最多为10000。
例如:

输入:
[1,2,3]

输出:
2

说明：
只有两个动作是必要的（记得每一步仅可使其中一个元素加1或减1）：

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

"""


def minMoveII(nums):
    """
    最小次数移动使得元素相等II
    分析： 和I的主要区别是，每次移动可以加1或者减1，I题中只能加1
        在这种情况下，针对有序数组，可以采用二分取中的方法，对于中间的数，计算左右索引位置数与中间索引位置数的diff，统计moves
    :param nums:
    :return:
    """
    nums = sorted(nums)

    L = len(nums)
    mid = int(L / 2)
    leftmoves, rightmoves = 0, 0

    for i in range(L):
        if i < mid:
            leftmoves = leftmoves + nums[mid] - nums[i]
        elif i > mid:
            rightmoves = rightmoves + nums[i] - nums[mid]

    return leftmoves + rightmoves


if __name__ == '__main__':
    print(minMoveII(nums=[1, 2, 3]))
