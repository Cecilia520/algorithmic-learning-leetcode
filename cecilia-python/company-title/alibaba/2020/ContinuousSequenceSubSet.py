#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ContinuousSequenceSubSet.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/30 22:12   cecilia      1.0       连续序列的所有子集的最大值的期望

问题描述：
小强得到了一个长度为n的序列，但他只对非常大的数字感兴趣，因此，他想随机选择
这个序列的一个连续子序列，并求出这个序列的最大值，请你告诉他这个最大值的期望值是多少?
对于连续子序列的定义：比如长度为3的序列2，5，6，他的连续子序列有{2},{5},{6},{2,5},{5,6},{2,5,6}

输入描述：
> 第一行数字n代表序列长度
> 接下来一行n个数字来描述这个序列
> 1 <= n <= 1000000

输出描述：
> 得到的期望值，浮点数，小数点保留6位

示例：
> 输入：
> 3
> 1 2 3

> 输出：2.333333
> 解释：所有连续子序列有{1},{2},{3},{1,2},{2,3},{1,3},{1,2,3},最大值分别是1，2，2，3，3，3，期望为2.333333

"""
from typing import List


class Solution:
    def __init__(self):
        self.all_subsets = [[]]

    def getAllSubSets(self, nums: List[int]) -> List[List[int]]:
        """
        找出连续序列的所有满足条件的子集
        思维方式：窗口滑动。
        :param nums:
        :return:
        """
        self.all_subsets = [nums]
        for i in range(1, len(nums)):
            start, end = 0, start + i
            while end <= len(nums):
                self.all_subsets.append([nums[i] for i in range(start, end)])
                start += 1
                end += 1

    def continuousSequenceSubSetII(self, nums: List[int]) -> int:
        """
        找出连续子序列的所有子集（子集中两个元素的值不能超过1）对应的最大值的期望
        :param n:
        :param nums:
        :return:
        """
        self.getAllSubSets(nums)

        L = len(self.all_subsets)

        max_list = [max(self.all_subsets[i]) for i in range(L)]

        max_sum = 0
        for num in max_list:
            max_sum += num

        E = round(max_sum / L, 6)

        return E


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    print(s.continuousSequenceSubSetII(nums=nums))
