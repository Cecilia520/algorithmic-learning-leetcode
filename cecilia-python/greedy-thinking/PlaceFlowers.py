#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PlaceFlowers.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/7 14:33   cecilia      1.0        种花问题

问题描述：
    假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在香菱的地块中，否则因为争夺水源而死亡。
给定一个花坛数组，由0和1组成，其中0表示没有种植花卉，1表示种植了花卉，能否在不打破规则的情况下种入n朵花？能就返回True，否则返回False。

示例 1:

输入: flowerbed = [1,0,0,0,1], n = 1
输出: True
示例 2:

输入: flowerbed = [1,0,0,0,1], n = 2
输出: False

注意:
1. 数组内已种好的花不会违反种植规则。
2. 输入的数组长度范围为 [1, 20000]。
3. n 是非负整数，且不会超过输入数组的大小。
"""


def canPlaceFlower(flowerbed, n) -> bool:
    """
    判断是否能种n朵花
    解决方案：贪心法
    解决思路：遍历数组，如果判断当前数据是0，那么判断左右两边的数据是否是0，如果均满足，那么count+1，否则count不变;
    最后如果count>=n，那么表示返回True
    :param flowerbed:数组
    :param n: 需要种入的花的数目
    :return:
    算法分析：时间复杂度O(N),空间复杂度O(1)
    """
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (
                i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            # 注意：如果当前满足，就将当前的值修改为1
            flowerbed[i] = 1
            count += 1
            # 常数循环提前终止, 优化计算时间,由最开始的N变成了循环的次数
            if count == n:
                return True
    return False


def canPlaceFlower1(flowerbed, n) -> bool:
    """
    判断是否能种n朵花
    解决方案：贪心法
    在上面，有个很大的问题需要注意的是边界问题，那么参考某个大佬的解题思路，可以采取补0的方法，消除边界带来的问题
    :param flowerbed:数组
    :param n: 需要种入的花的数目
    :return:
    算法分析：时间复杂度O(N),空间复杂度O(1)
    """
    # 前后补零解决边界问题
    flowerbed = [0] + flowerbed + [0]
    count = 0
    i = 1
    while i < len(flowerbed) + 1:
        if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
            count += 1
            # 可以种花，则需要间隔一个位置，所以+2
            i += 2
        else:
            i += 1
        if count >= n:
            return True
    return False




if __name__ == '__main__':
    print(canPlaceFlower1(flowerbed=[1, 0, 0, 0, 0, 0, 0, 0, 0, 1], n=2))
