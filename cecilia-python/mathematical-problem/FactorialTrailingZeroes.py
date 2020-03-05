#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   FactorialTrailingZeroes.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/3 19:03   cecilia      1.0       统计阶乘结果尾数中零的数量
问题描述：
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。

示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
> 说明: 你算法的时间复杂度应为 O(log n) 。

思路分析：
  本题实质上是规律总结的数学问题，对于尾数出现0，我们发现当出现10或者2*5时，尾数会出现一个0，
  也就是说寻找（2，5）的对数，有多少对2*5，那么尾数存在多少个0，其中10也可以等同于2*5=10；
  每隔2个数，出现一个2，每隔5个数，出现一个5，那么看起来2*5的对数就等同于有多少个5，也就是找5的倍数有多少个,即N = N / 5；
  优化点：每隔5个数，出现一个5，那么每隔25个数，出现2个5，是前一个数+1，类似的，每隔125，出现3个5......,即我们只需要统计计算N/5计算了多少次即可
"""
def factorialTrailingZeroes(n):
    """
    统计阶乘尾数有多少个0（2019年小红书面试出现过）
    :param n:
    :return:
    """
    count = 0
    while n >= 5:
        n = n // 5
        count = count + n
    return count

if __name__ == '__main__':
    print(factorialTrailingZeroes(n=12))
