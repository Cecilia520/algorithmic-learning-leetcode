#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   AssignCookies.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/4 17:37   cecilia      1.0         分配饼干
问题描述：
假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。对每个孩子 i ，都有一个胃口值 gi ，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j ，都有一个尺寸 sj 。如果 sj >= gi ，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。
注意：
你可以假设胃口值为正。
一个小朋友最多只能拥有一块饼干。
示例1：
输入: [1,2,3], [1,1]
输出: 1
解释:
你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
所以你应该输出1。

示例2：
输入: [1,2], [1,2,3]

输出: 2

解释:
你有两个孩子和三块小饼干，2个孩子的胃口值分别是1,2。
你拥有的饼干数量和尺寸都足以让所有孩子满足。
所以你应该输出2.

分析思路：
1.给一个孩子的饼干应当尽量小并且又能满足该孩子，这样大饼干才能拿来给满足度比较大的孩子。
2.因为满足度最小的孩子最容易得到满足，所以先满足满足度最小的孩子。
"""


def assignCookies(grids, sizes):
    """
    先满足满足度最小的孩子
    :param grids: 小孩子的胃口数组
    :param sizes: 饼干的尺寸数组
    只有饼干的大小大于等于一个孩子的满足度，该孩子才会获得满足，因此分别对两个数组按照从小到大进行排序。
    :return:
    """
    # 先分别排序
    sortgrids = sorted(grids)
    sortsizes = sorted(sizes)

    # 比较胃口和饼干尺寸大小，当饼干的大小大于等于一个孩子的满足度，该孩子才会获得满足
    gi = 0
    sj = 0
    while gi < len(sortgrids) and sj < len(sortsizes):
        if sortgrids[gi] <= sortsizes[sj]: # 能够满足一个孩子的胃口
            gi += 1 # 孩子胃口+1
        sj += 1 # 吃了一个饼干
    return gi


if __name__ == '__main__':
    grids = [3, 1, 2]
    sizes = [3]
    print(assignCookies(grids, sizes))
