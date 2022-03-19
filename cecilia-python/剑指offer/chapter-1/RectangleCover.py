#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   RectangleCover.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/9 10:09   cecilia      1.0        矩形覆盖（考察数学规律）
问题描述：
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

比如n=3时，2*3的矩形块有3种覆盖方法：
三竖立
左一竖立右二横
左二横右一竖立
"""
'''
该题实际上属于数学归类的题型，经过规律类推发现符合斐波那契数列的规律
'''
class Solution:
    def RectangleCover(self, n)->int:
        if n <= 0:
            return 0
        if n == 1:
            return 1

        res = []
        if n >= 2:
            res.append(1)
            res.append(2)
            for i in range(1, n):
                res.append(res[i]+res[i-1])
        return res[n-1]

if __name__ == '__main__':
    s = Solution()
    print(s.RectangleCover(n=3))