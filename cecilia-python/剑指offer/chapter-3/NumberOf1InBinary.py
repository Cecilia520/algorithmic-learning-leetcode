#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   NumberOf1InBinary.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/20 9:58   cecilia      1.0        二进制中1的个数（位运算）
问题描述：
请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。

示例 1：

输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
示例 2：

输入：00000000000000000000000010000000
输出：1
解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
示例 3：

输入：11111111111111111111111111111101
输出：31
解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

'''
解决问题的关键点：
    1. 位运算的定义
        - 若n&1==0,那么n二进制最右一位为0；
        - 若n&1==1,那么n的二进制最右一位位1.
'''


class Solution:
    def hammingWeight_0(self, n: int) -> int:
        """
        逐位判断
        根据n的最后一位是否是1，然后计数，因为0&1=0，最后右移循环判断
        :param n:
        :return:
        复杂度分析：时间复杂度O（logn^2）,空间复杂度O（1）
        """
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res

    def hammingWeight(self, n: int) -> int:
        """
        巧用n&（n-1）
        n的二进制最右边的1变成0，此1右边的0都变成1
        n&(n-1)二进制数字n最右边的1变成0，其余的不变
        比如：
        n = 10101000
        n-1 = 10100111
        n&(n-1) = 10100000
        :param n:
        :return:
        复杂度分析：时间复杂度O（M），M表示每轮消去1的次数M；空间复杂度O（1）
        """
        cnt = 0
        while n:
            cnt += 1
            n &= n - 1  # 每次消去一个1，就记录1
        return cnt

    def hammingWeight_1(self, n: int) -> int:
        """
        直接调用库函数bin
        :param n:
        :return:
        """
        return bin(n).count("1")


if __name__ == '__main__':
    s = Solution()
    n = 9
    print(s.hammingWeight_0(n))
    print(s.hammingWeight(n))
    print(s.hammingWeight_1(n))
