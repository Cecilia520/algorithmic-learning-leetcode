#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   Fibonacci.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/9 9:58   cecilia      1.0         斐波那契数列
问题描述：
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def Fibonacci(self, n:int)->int:
        if n < 2:
            return n
        res = []
        if n >= 2:
            res.append(1)
            res.append(1)
            for i in range(2, n):
                tmp = res[i-1]+res[i-2]
                res.append(tmp)
        return res[n-1] % 1000000007

if __name__ == '__main__':
    n = int(input())
    s = Solution()
    print(s.Fibonacci(n))
