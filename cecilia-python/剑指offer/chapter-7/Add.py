#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   Add.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/8/21 16:48   cecilia      1.0       不用加法运算做加法（位运算）
问题描述：

"""
'''
思路总结：
    不用加法做和运算：
        1. 正数的补码是本身；负数的补码和Oxffffffff做与运算；
        2.非进位和==a与b的异或运算，即a^b;
        3.进位和等于(a&b)<<1；
        4.最终的和值为非进位和+进位和
'''


class Solution:
    def add(self, a: int, b: int) -> int:
        """
        不用加法运算做加法
        :param a:
        :param b:
        :return:
        复杂度分析：时间复杂度O（）
        """
        x = 0xffffffff
        a = a & x
        b = b & x
        while b != 0:
            # a = a ^ b
            # b = (a & b) << 1 & x
            # 上面和下面的写法不同，计算结果也不相同，并排写法能同时运算结果，互不影响，分别计算非进位和和进位和
            a, b = (a ^ b), (a & b) << 1 & x
            print("a:{}".format(a))
            print("b:{}".format(b))
        return a if a <= 0x7fffffff else ~(a ^ x) # 若补码 a 为负数（ 0x7fffffff 是最大的正数的补码 ），需执行 ~(a ^ x) 操作，将补码还原至 Python 的存储格式,~(a ^ x) 是将 32 位以上的位取反，1 至 32 位不变。


if __name__ == '__main__':
    s = Solution()
    print(s.add(a=1, b=2))