#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   CheckSubarraySum-560.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/11 21:27   cecilia      1.0       判断当前是否存在连续子数组和的和是指定的K——微软面试出现过
问题描述：leetcode-523
给定一个包含非负数的数组和一个目标整数 k，编写一个函数来判断该数组是否含有连续的子数组，其大小至少为 2，总和为 k 的倍数，即总和为 n*k，其中 n 也是一个整数。

示例 1:

输入: [23,2,4,6,7], k = 6
输出: True
解释: [2,4] 是一个大小为 2 的子数组，并且和为 6。
示例 2:

输入: [23,2,6,4,7], k = 6
输出: True
解释: [23,2,6,4,7]是大小为 5 的子数组，并且和为 42。

要求：时间复杂度为O(N)  <如果使用传统暴力法，面试就会凉凉拉>

https://leetcode-cn.com/problems/continuous-subarray-sum/solution/lian-xu-de-zi-shu-zu-he-by-leetcode/

"""


def checkSubarrayKSum(nums, k) -> bool:
    """
    判断当前数组种是否存在连续子数组和为指定的K倍
    思路分析：
        遍历数组，将和存储在哈希表中，然后判断和%k的余数是否在哈希表中，如果在哈希表中，那么代表存在，返回True；否则继续寻找。
        关键点：每次求和计算余数是否在已存在的哈希表中，并且不是当前的位置，那么可以说明存在连续子序和为k的整数倍
    :param nums:
    :param k:
    :return:
    算法分析：时间复杂度O(N),空间复杂度O(min(n,k))
    """
    if len(nums) < 2:
        return False

    dict = {}
    dict[0] = -1  # 初始化

    sum = 0

    for i in range(len(nums)):
        sum = sum + nums[i]
        if k != 0:
            sum = sum % k

        if sum not in dict:
            dict[sum] = i # 如果不存在哈希表中，则添加到dict中
        else:
            tmp = i - dict.get(sum) # 如果存在，判断是否是当前位置的值，如果不是，那么返回True
            if tmp > 1:
                return True
    return False


if __name__ == '__main__':
    print(checkSubarrayKSum(nums=[23, 2, 6, 4, 7], k=6))
