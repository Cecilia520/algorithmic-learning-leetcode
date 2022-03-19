#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   34.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/30 18:04   cecilia      1.0         None
"""

class Solution:
    def getDis(self, n, m, nums):
        """
        所有分配的方案数
        :param n:糖果数
        :param m:糖罐个数
        :param nums:分配的糖果的颜色
        :return:
        """
        if not n or not m:
            return 0
        if n == 1 and m > 0:
            return 1
        cnt = len(set(nums)) # 颜色种类数
        print(cnt)





if __name__ == '__main__':
    s = Solution()
    n, m = map(int, input().strip().split())
    nums = list(map(int, input().strip().split()))
    print(s.getDis(n, m, nums))
