#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   NextGreaterElement-II.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/7 22:12   cecilia      1.0        循环数组中比当前元素大的下一个元素
问题描述：
给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

示例 1:

输入: [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数；
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
注意: 输入数组的长度不会超过 10000。

"""
def nextGreaterElement(nums):
    """
    记录下一个元素的最大值
    思路分析：单调栈
        用单调栈求解，此处栈内记录的是 nums 元素的下标
           1.直接将 nums 复制两倍
           2.判断栈顶元素和当前元素的大小
            若栈顶元素 > 当前元素：当前元素入栈
            若栈顶元素 < 当前元素：弹出栈顶元素，并记录栈顶元素的下一个更大元素为当前元素
    算法分析：时间复杂度O(N),空间复杂度O(N)
    :param nums:
    :return:
    """
    nums_length = len(nums)
    res_list = [-1 for _ in range(nums_length)]
    stack = list()

    double_nums = nums + nums
    for index, num in enumerate(double_nums):

        while stack and nums[stack[-1]] < num:
            res_list[stack[-1]] = num
            stack.pop()
        if index < nums_length:
            stack.append(index)
    return res_list


if __name__ == '__main__':
    print(nextGreaterElement(nums=[1,2,1]))
