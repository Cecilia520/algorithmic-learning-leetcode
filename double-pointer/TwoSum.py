#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   TwoSum.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/13 14:10   cecilia      1.0       有序数组的TwoSum（）
问题描述：
在有序数组中找出两个数，使它们的和为 target。
函数TowSum应该返回两个数字的索引，以便他们加起来到特定的目标，其中index1必须小于index2

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""


def TwoSum(numbers, target):
    """
    有序数组中找出两个数，使之他们的和为target
    :param numbers:输入数据
    :param target:目标数据
    :return:
    解题思路：使用双指针，一个指针指向较小的元素，一个指向较大的元素。指向较小的元素从头开始遍历，指向较大的元素从头开始遍历。
    - 如果当前指针指向的两个元素和等于目标值sum==target，那么返回这两个元素的索引；
    - 如果sum < target,就移动较小的元素，使得和变得大一些；
    - 如果 sum > target,就移动较大的元素，使得和变得更小一些。
    算法分析：数组中的元素最多遍历一次，时间复杂度为 O(N)。只使用了两个额外变量，空间复杂度为 O(1)。
    """
    if numbers is None:
        return "Please input the integers."
    i = 0
    j = len(numbers) - 1
    while i < j:
        sum = numbers[i] + numbers[j]
        if sum == target:
            return [i, j]
        elif sum < target:
            i = i + 1
        elif sum > target:
            j = j - 1
    return "i 必须小于 j！"
    # print("i 必须小于 j！")


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 18
    output = TwoSum(numbers, target)
    print(output)
