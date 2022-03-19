#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   CutRope-2.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/10 14:32   cecilia      1.0       剪绳子-2（考察数学推导规律以及快速幂的方法）
问题描述：
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为 k[0],k[1]...k[m - 1] 。请问 k[0]*k[1]*...*k[m - 1] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
示例 1：
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1

示例 2:
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
'''
该题思路和CutRope相差不多，但是主要是考察对于大数求余上面做些优化时间复杂度，其解决方案主要有两种，——
- 第一种：循环求余法。(x^a) % p
- 第二种：快速幂求余。x^a % p = 
当a为偶数时，x^a % p = (x^2 % p)^(a//2) % p
当a为奇数时，x^a % p = ((x%p)(x^(a-1) % p))%p = (x(x^2 % p))^(a//2) % p
'''


class Solution:
    def CutRope2(self, n) -> int:
        """
        剪绳子-2
        快速幂求余法
        :param n:
        :return:
        """
        if n <= 3:
            return n - 1
        a, b, x, p, reminder = n // 3 - 1, n % 3, 3, 1000000007, 1
        # 快速幂求余
        while a > 0:
            if a % 2:
                reminder = (reminder * x) % p
            x = x ** 2 % p
            a //= 2
        if b == 0:
            return (reminder * 3) % p  # 3^(a+1) % p
        if b == 1:
            return (reminder * 4) % p  # 3^a * 4 % p
        return (reminder * 6) % p  # 3^(a+1) * 2 % p

    def CutRope_2(self, n):
        """
        循环求余法，其中3表示切3段是最佳段数
        :param n:
        :return:
        """
        if n <= 3:
            return n - 1
        res = 1
        p = 1000000007
        while n > 4:
            res = res * 3 % p
            n -= 3
        return int(res * n % p)


if __name__ == '__main__':
    s = Solution()
    print(s.CutRope2(n=10))
