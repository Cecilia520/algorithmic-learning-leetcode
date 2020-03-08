#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   NextGreaterElement-I.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/7 22:17   cecilia      1.0         下一个更大元素 I
问题描述：
给定两个没有重复元素的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出-1。

示例 1:
输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
    对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
    对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。

示例 2:
输入: nums1 = [2,4], nums2 = [1,2,3,4].
输出: [3,-1]
解释:
    对于num1中的数字2，第二个数组中的下一个较大数字是3。
    对于num1中的数字4，第二个数组中没有下一个更大的数字，因此输出 -1。
注意:
nums1和nums2中所有元素是唯一的。
nums1和nums2的数组大小都不超过1000。

"""
def nextGreaterElement(nums1, nums2):
    """
    记录下一个元素的最大值
    思路分析：单调栈+hashmap
       1.遍历nums2，维护一个递减栈；
       2.当得到一个更大的数的时候，将栈里小于它的数都放到HashMap当中；
       3.遍历nums1，对每一项查找哈希表，找到第一个比它大的数，并返回一个列表作为答案。如果在哈希表中不存在则返回默认值-1。
    :param num1:
    :param num2:
    :return:
    """
    stack = []
    hashmap = dict()
    for i in nums2:
        while len(stack) != 0 and stack[-1] < i: hashmap[stack.pop()] = i
        stack.append(i)
    return [hashmap.get(i, -1) for i in nums1]
