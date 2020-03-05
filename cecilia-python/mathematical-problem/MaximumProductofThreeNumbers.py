#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MaximumProductofThreeNumbers.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/3 19:09   cecilia      1.0        找出数组中的乘积最大的三个数

问题描述：
    给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:

输入: [1,2,3]
输出: 6
示例 2:

输入: [1,2,3,4]
输出: 24
注意:

>> 给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。
"""


def maximumProductofThreeNumbers(nums):
    """
    计算三个整数的最大乘积
    注意：此处和三个整数的最大和有区别，三个整数的最大和可以考虑使用递归的方法先求初多个三个和的数组，
         然后多次比较找到最大和的值，乘积需要考虑两个负数的乘积是正数的情况
    :param nums:
    :return:
    算法分析：
    """
    nums = sorted(nums)
    L = len(nums)
    return max(nums[0] * nums[1] * nums[L - 1], nums[L - 1] * nums[L - 2] * nums[L - 3])


if __name__ == '__main__':
    print(maximumProductofThreeNumbers(nums=[-4, -3, -2, -1, 60]))
