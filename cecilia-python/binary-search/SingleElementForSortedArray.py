#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   SingleElementForSortedArray.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/15 13:30   cecilia      1.0        在一个有序数组中，只出现一次的元素，找出来

问题描述：
给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。

示例：
示例 1:
输入: [1,1,2,3,3,4,4,8,8]
输出: 2

示例 2:
输入: [3,3,7,7,10,11,11]
输出: 10

注意: 您的方案应该在 O(logn)时间复杂度和 O(1)空间复杂度中运行。

"""


def singleElementForSortedArray(nums) -> int:
    """
    在一个有序数组中寻找只出现一次的单个元素
    分析：
        令 index 为 Single Element 在数组中的位置。在 index 之后，数组中原来存在的成对状态被改变。
           1.如果 m 为偶数，并且 m + 1 < index，那么 nums[m] == nums[m + 1]；
           2.否则m + 1 >= index，那么 nums[m] != nums[m + 1]。
        从上面的规律可以知道：
          1.如果 nums[m] == nums[m + 1]，那么 index 所在的数组位置为 [m + 2, h]，此时令 l = m + 2；
          2.如果 nums[m] != nums[m + 1]，那么 index 所在的数组位置为 [l, m]，此时令 h = m。
        因为 h 的赋值表达式为 h = m，那么循环条件也就只能使用 l < h 这种形式。
    :param nums: 给定的数组
    :return:
    """
    l, h = 0, len(nums) - 1

    while l < h:
        mid = int(l + (h - l) / 2)
        # 保证 l/h/m 都在偶数位，使得查找区间大小一直都是奇数
        if mid % 2 == 1:
            mid -= 1
        if nums[mid] == nums[mid + 1]:
            l = mid + 2
        else:
            h = mid
    return nums[l]


if __name__ == '__main__':
    nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    print(singleElementForSortedArray(nums))
