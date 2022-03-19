#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ClimbStairs.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/27 15:03   cecilia      1.0        爬楼梯
问题描述：假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
def climbStairs(n: int) -> int:
    """
    爬楼梯
    :param n:
    :return:
    """
    if n <= 2:
        return n
    result = [0] * n
    if n > 2:
        for i in range(2, n):
            result[0] = 1
            result[1] = 2
            result[i] = result[i - 1] + result[i - 2]
    return result[n - 1]

if __name__ == '__main__':
    print(climbStairs(n=5))