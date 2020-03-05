#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MinimumMovesToEqualArrayElementsI.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/5 11:56   cecilia      1.0        最小移动次数使得数组元素相等I

给定一个长度为 n 的非空整数数组，找到让数组所有元素相等的最小移动次数。每次移动可以使 n - 1 个元素增加 1。

示例:

输入:
[1,2,3]

输出:
3

解释:
只需要3次移动（注意每次移动会增加两个元素的值）：

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

"""
def minMove(nums):
    """
    最小次数移动使得元素相等I
    :param nums:
    :return:
    """
    nums = sorted(nums)
    moves = 0
    for i in range(1, len(nums)):
        diff = moves + nums[i] - nums[i - 1]
        # 修改赋值num[i]
        nums[i] = nums[i] + moves
        # 汇总
        moves = moves + diff
    return moves

if __name__ == '__main__':
    print(minMove(nums=[1,2,3]))
