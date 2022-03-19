#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   SubarrayKSum-523.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/11 21:23   cecilia      1.0      连续子序和是指定的K的个数
问题描述：
对应leetcode-560：
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。

要求：时间复杂度为O(n)——哈希表存储
    一般的暴力法的时间复杂度是O(N^2),不合格

链接：https://leetcode-cn.com/problems/subarray-sum-equals-k/solution/he-wei-kde-zi-shu-zu-by-leetcode/

"""
import collections


def subArraySum(nums, k) -> int:
    """
    思路方法：
        1. 创建和初始化一个默认的hashmap（字典），用于存储所有可能性的索引的累计总和以及相同累加和发生的次数。
           如果累计总和，在索引 i 和 j 处相差 k，即 sum[i] - sum[j] = ksum[i]−sum[j]=k，则位于索引 i 和 j 之间的元素之和是 k。
        2. 遍历判断
    :param nums:
    :param k:
    :return:
    算法分析：时间复杂度O(N),空间复杂度O(N)
    """
    sum_dict = collections.defaultdict(int)
    sum_dict[0] = 1
    print(sum_dict)

    res, cur = 0, 0
    result = []

    for num in nums:
        cur += num  # 累加
        res += sum_dict[cur - k]
        result.append(res)
        sum_dict[cur] += 1
    return res


if __name__ == '__main__':
    print(subArraySum(nums=[1, 1, 1], k=2))
