#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   NetherlandsFlagOfSortColors.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/3 12:07   cecilia      1.0         荷兰国旗问题之颜色排序

问题背景：
荷兰国旗包括三种颜色：红、白、蓝；
有三种颜色的球，算法的目标就是将这三种颜色的球按照颜色顺序正确地排列。它其实是三向切分快速排序的一种变种，在三向切分快速排序中，每次切分都将数组分成三个区间：小于切分元素、等于切分元素、大于切分元素，而将该算法是将数组分成三个区间：等于红色、等于白色、等于蓝色

问题描述
1.按照颜色进行排序
给定一个包含红色、白色和蓝色，一共n个元素的数组，原地对它们进行排序，使得相同颜色地元素相邻，并按照红色、白色、蓝色排序。
可以使用0、1和2分别表示红色、白色和蓝色。

注意：不能使用代码库中地排序函数来解决问题！！！

示例：
输入：[2,0,2,1,1,0]
输出：[0,0,1,1,2,2]

进阶思路：
- 一个最直观地解决方案就是使用计算排序的两躺扫描算法；
首先，迭代计算出0、1和2地元素的个数，然后按照0、1、2的排序，重写当前的数组
- 仅使用常数空间的一趟扫描算法。
"""


def netherlandsFlagOfSortColors(nums) -> None:
    """
    荷兰国旗问题——颜色排序
    :param nums:
    :return:
    算法分析：
        时间复杂度 :由于对长度 NN的数组进行了一次遍历，时间复杂度为O(N)；
        空间复杂度：使用了常数空间，空间复杂度O(1)
    """
    # 初始化三个指针，p0、curr、p2
    # 对于所有的idx<p0,idx>p2
    p0 = 0
    curr = 0
    p2 = len(nums) - 1

    while (curr <= p2):
        if nums[curr] == 0:
            nums[p0], nums[curr] = nums[curr], nums[p0]
            p0 += 1
            curr += 1
        elif nums[curr] == 2:
            nums[p2], nums[curr] = nums[curr], nums[p2]
            p2 -= 1  # 此处不需要curr++，因为curr左边的值已经扫描过了，所以curr要++继续扫描下一位，而与p2交换的值，curr未扫描，要停下来扫描一下，所以curr不用++
        else:
            curr += 1
    return nums


if __name__ == '__main__':
    nums = [2, 0, 1]
    print(netherlandsFlagOfSortColors(nums))
