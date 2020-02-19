#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   SolveSqrt.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/15 13:25   cecilia      1.0       求开方
问题描述：
求一个整数的开方的值
思路：
折半查找法：定好l和h，比较mid和x/mid的值的大小，最后返回h

示例：
Input: 4
Output: 2

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.
一个数 x 的开方 `sqrt `一定在 0 ~ x 之间，并且满足 sqrt == x / sqrt。可以利用二分查找在 0 ~ x 之间查找 sqrt。
对于 x = 8，它的开方是 2.82842...，最后应该返回 2 而不是 3。在循环条件为 l <= h 并且循环退出时，h 总是比 l 小 1，也就是说 h = 2，l = 3，因此最后的返回值应该为 h 而不是 l。
"""


def solveSqrt(x):
    """
    求开方
    提示：一个数 x 的开方 `sqrt `一定在 0 ~ x 之间，并且满足 sqrt == x / sqrt。
    :param x:
    :return:
    """
    if x <= 1:
        return x

    # sqrt(x)一定在[0,x]之间
    l = 1
    h = x

    while l <= h:
        mid = int(l + (h - l) / 2)  # 必须保证是int
        sqr = int(x / mid)
        if mid == sqr:
            return mid  # 刚好查找到
        elif mid > sqr:  # 表示sqr值落在[l,m]的区间中
            h = mid - 1
        else:
            l = mid + 1
    return h  # 在循环条件为 l <= h 并且循环退出时，h 总是比 l 小 1，也就是说 h = 2，l = 3，因此最后的返回值应该为 h 而不是 l。


if __name__ == '__main__':
    x = 8
    print(solveSqrt(x))