#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ResellingLoot.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/7 11:44   cecilia      1.0        倒卖战利品
问题描述：
在游戏中，击败魔物后，薯队长获得了N件宝物，接下来得把这些宝物卖给宝物回收员来赚点小钱。这个回收员有个坏毛病，
每次卖给他一件宝 物后，之后他就看不上比这件宝物差的宝物了。在这个世界中，衡量宝物的好坏有两个维度，稀有度X和实用度H，
回收员在回收一个宝物A 后，下一个宝物的稀有度和实用度都不能低于宝物A。那么薯队长如何制定售卖顺序，才能卖给回收员宝物总个数最多。

输入描述：第一行一个正整数N。 接下来N行。每行两个整数分别表示X    和    H X1    H1 X2    H2 … XN    HN
输入限制： 对于70%的数据：
0<N<10^4
0<Xi<10^6
0<Hi<10^6
100%的数据：
0<N<10^6
0<Xi<10^6
0<Hi<10^6

输出：一个整数，表示最多可以卖出的宝物数

输入例子1:
4
3 2
1 1
1 3
1 2

输出例子1:
3
"""
'''
该题主要是根据两个指标如何对目前的数据制定顺序才能获得最多宝物总数，其中涉及到排序、LIS（最长上升子序列问题）问题
'''
class Solution:
    def binary_search(self, nums, low, high,target):
        """
        根据指定的数据寻找相应的位置
        @param: nums
        @param: low
        @param: high
        @param: target
        """
        mid = 0
        while low < high:
            mid = low + int((high - low)/2)
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low
    def LIS(self, N, treasures):
        """
        最长上升子序列
        @param: N
        @param: treasures
        """
        res = [] #记录单调递增数组
        for i in range(N):
            if not res or treasures[i] > res[-1]:
                 res.append(treasures[i])
            else:
                idx = self.binary_search(res, 0, len(res), treasures[i])
                res[idx] = treasures[i]
        return len(res)
if __name__ == '__main__':
    N = int(input().strip())
    treasures = []
    for i in range(N):
        treasures.append(list(map(int,input().strip().split())))
    treasures.sort()
    H = [x[1] for x in treasures]
    s = Solution()
    print(s.LIS(N, H))