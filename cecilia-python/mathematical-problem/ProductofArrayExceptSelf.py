#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ProductofArrayExceptSelf.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/3 19:08   cecilia      1.0         乘积数组

问题描述：
  给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，
    其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

"""


def productofArrayExceptSelf(nums):
    """
    乘积数组
    解决方案：遍历数组，先对当前索引i前i-1个数进行乘积，然后再倒序遍历数组对右边进行乘积
    :param nums:
    :return:
    算法分析：时间复杂度O(N),空间复杂度O(1)
    """
    L = len(nums)
    result = [0] * L
    result[0] = 1

    # 顺序遍历数组，计算i左边的数据地乘积
    for i in range(1, L):
        result[i] = result[i - 1] * nums[i - 1]

    Right = 1
    # 倒序遍历数组，计算右边的乘积
    for j in range(L-1, -1, -1):
        result[j] = result[j] * Right
        Right = Right * nums[j]

    return result


if __name__ == '__main__':
    print(productofArrayExceptSelf(nums=[1, 2, 3, 4]))
