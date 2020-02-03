#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   SumSquareNumbers.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/13 16:34   cecilia      1.0      两个数的平方和
问题描述：判断一个非负整数是否为两个整数的平方和。
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
"""
import math
def SumSquareNumbers(target):
    """
    判断一个非负整数是否为两个整数的平方和
    :param target:目标值
    :return:
    解题思路：设定一个双指针，刚开始可以给左指针初始化为0，关键在于右指针的初始化，从而实现剪枝，降低时间复杂度。
    若0^2+x^2=target,那么右指针初始化则是sart(target),此时时间复杂度也是O(sqrt(target)),空间复杂度为O(1)
    """
    if target < 0:
        return False
    i = 0
    j = int(math.sqrt(target))
    while i <= j:
        sum = i * i + j * j
        if sum == target:
            print("i:{}, j:{}".format(i, j))
            return True
        elif sum > target:
            j = j - 1
        else:
            i = i + 1
    print('该非负整数不能为两个整数的平方和！ ')
    return False


if __name__ == '__main__':
    SumSquareNumbers(20) # 2 * 2 + 4 * 4 = 20
