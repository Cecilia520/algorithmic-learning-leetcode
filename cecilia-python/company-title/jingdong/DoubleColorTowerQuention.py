#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   DoubleColorTowerQuention.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/18 12:22   cecilia      1.0       双色塔配色方案
问题描述：
链接：https://www.nowcoder.com/questionTerminal/23a0c9e5b3eb4f37b9615766f0286e0c?orderByHotValue=1&page=1&onlyReference=false
来源：牛客网

现在有红，绿两种颜色的石头，现在我们需要用这两种石头搭建一个塔，塔需要满足如下三个条件：
1．第1层应该包含1块石头，第2层应该包含两块，第 i 层需要包含 i 块石头。
2．同一层的石头应该是同一个颜色（红或绿）。
3．塔的层数尽可能多。
问在满足上面三个条件的前提下，有多少种不同的建造塔的方案，
当塔中任意一个对应位置的石头颜色不同，我们就认为这两个方案不相同。石头可以不用完。

输入描述:
输入仅包含两个正整数，分别表示红和绿砖块的数量a，b（0<=a,b<=2*10^5,a+b>=1）。


输出描述:
输出和仅包含一个正整数，表示不同的方案数对1000000007取模的结果。

示例1
输入 4 6
输出 2
"""
import math
import sys


class Solution:
    def __init__(self):
        self.MOD = 1000000007
        self.N = 200000

    def doubleColorTower(self, a, b):
        """
        思路：
        当两种颜色的砖的数目不相同时，首先先使用数量较少的颜色的砖和另一种颜色的砖尽可能的组成level；直到数目少的颜色的砖用完为止；
        当两种演的砖相同时，依次累加直到任意一种颜色先用完为止。
        这里的状态：dp[i][j]可以表示为前level层放j个砖头的值，前一层可能不放数目较少的颜色的砖，也可可能放数目较少的砖，总的数目就是不放和放的情况下的累加和，
。       其中i=level&1，要么是0，要么是1
        状态压缩：在这里可以将二维数组压缩为一维数组，dp[i]表示
        :param a 红色砖的数目
        :param b 绿色砖的数目
        :return:
        """
        dp = [0 for _ in range(self.N + 1)]

        dp[0] = dp[1] = 1

        level = int(math.sqrt(2 * (a + b)))  # 总的层数

        if a > b:
            a, b = b, a

        sum_num = 1

        global lower
        global upper

        for i in range(2, level + 1):
            sum_num += i

            tmp_upper = min(sum_num, a)
            tmp_lower = max(sum_num - b, 0)

            if tmp_lower > tmp_upper:
                break

            upper = tmp_upper
            lower = tmp_lower

            for j in range(upper, i+2, -1):
                dp[j] = (dp[j] + dp[j-i]) % self.MOD #要么上一层放绿色砖，要么不放

            dp[i] += 1

        print(dp)

        # 假设红色的石头数量最少，那么先用全部的绿色石头和尽可能少的红色石头(lower)组成尽可能多的层数(level)，
        # 将红色石头的使用数量逐渐提高至红色石头总数(upper)，lower到upper的每种可能的总和就是所有情况。
        res = 0
        for j in range(lower, upper+1):
            res = (res + dp[j]) % self.MOD
        return res

if __name__ == '__main__':
    a, b = map(int, sys.stdin.readline().strip().split())
    s = Solution()
    res = s.doubleColorTower(a, b)
    print(res)