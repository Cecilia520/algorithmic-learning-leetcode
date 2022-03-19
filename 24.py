#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   24.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/13 9:56   cecilia      1.0         None
"""
class Solution:
    def search_minnum(self, num:int)->int:
        """
        查找最小降序正整数
        :@param num
        """
        if num <= 9 and num >= 1:
            return num
        i, j = 1, 10000000
        while i < j:
            mid = i + (j - i)//2
            if mid - num >= 1:
                j = mid
            else:
                i = mid + 1
            print("i:{}".format(i))
            print("j:{}".format(j))
        return j
if __name__ == '__main__':
    s = Solution()
    num = int(input().strip())
    print(s.search_minnum(num))