#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   JumpStairs-1.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/9 10:07   cecilia      1.0         跳台阶
问题描述：
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
示例 2：

输入：n = 7
输出：21

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
'''
当n=1时，只有1种跳法；
当n=2时，有2种跳法；
当n=3时，有（1+1+1）/（1+2）/（2+1）有3种跳法；
当n=4时，有（1+1+1+1）/（1+1+2）/（1+2+1）/（2+1+1）/（2+2）有5种跳法；
当n=5时，有(1+1+1+1+1)/(1+1+1+2)/(1+1+2+1)/(1+2+1+1)/(2+1+1+1)/(1+2+2)/(2+2+1)/(2+1+2)有8种跳法；规律类似斐波那契数列
F(n)= F(n-1)+F(n-2)
'''
class Solution:
    def JumpStairs(self, n)->int:
        """
        青蛙跳台阶问题
        :param n:
        :return:
        """
        if n == 1 or n == 0:
            return 1
        res = []
        MOD = 1000000007
        if n >= 2:
            res.append(1)
            res.append(2)
            for i in range(2, n):
                tmp = res[i-2] + res[i-1]
                res.append(tmp)
            print(res)
        return res[n-1] % MOD

if __name__ == '__main__':
    s = Solution()
    print(s.JumpStairs(n=int(input())))
