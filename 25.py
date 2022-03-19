#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   25.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/14 19:45   cecilia      1.0         None
"""


class Solution:
    def getNum2(self, m: int, n: int) -> int:
        if m < n:
            return 0
        m_num = 1
        n_num = 1
        for i in range(n):
            m_num = m_num * (m - i)
            n_num = n_num * (i + 1)
        return m_num // n_num

    def getNum(self, m: int, n: int) -> int:
        if m == n:
            return 1
        elif n == 1:
            return m
        else:
            return self.getNum(m - 1, n - 1) + self.getNum(m - 1, n)


if __name__ == '__main__':
    s = Solution()
    m, n = map(int, input().strip().split())
    print(s.getNum(m, n))
