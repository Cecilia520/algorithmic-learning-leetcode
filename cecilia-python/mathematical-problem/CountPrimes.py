#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   CountPrimes.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/21 17:17   cecilia      1.0        统计素数的个数
问题描述：统计所有小于非负整数 n 的质数的数量。
示例：
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7。
最高效的解决思路；
    埃拉托斯特尼筛法在每次找到一个素数时，将能被素数整除的数排除掉。
"""


def isPrime(n) -> bool:
    """
    判断当前的数是否是素数
    :param num:
    :return:
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def countPrimes(n):
    """
    统计素数的个数
    方法一：递归判断每一个数字是否是素数（是否被2整除）
    :param n:
    :return:
    """
    cnt = 0
    for i in range(2, n):
        if isPrime(i):
            cnt += 1
    return cnt


def countPrimes2(n) -> int:
    """
    方法二：埃拉托斯特尼筛选法
    算法思路：埃拉托斯特尼筛法在每次找到一个素数时，将能被素数整除的数排除掉。
    也就是说先干掉2的倍数，然后干掉3的倍数，（4是2的倍数，过滤），干掉5的倍数，（6是2和3的倍数），干掉7的倍数，一直到sqrt(n)
    :param n:
    :return:
    """
    if n < 2:
        return 0

    # 初始化质数
    isPrimes = [1] * n
    # print("isPrimes:{}".format(isPrimes))
    isPrimes[0] = isPrimes[1] = 0
    # 在 2 到 根号n 的范围内，当一个数是质数，将它所有的比n小的倍数设置成0
    for i in range(2, int(n ** 0.5) + 1):
        if isPrimes[i] == 1:
            # 切片[start: end: 间隔]，范围是start=<x<end
            isPrimes[i * i:n:i] = [0] * len(isPrimes[i * i:n:i])
            # print("isPrimes[i * i:n:i]:{}".format(isPrimes[i * i:n:i]))
    return sum(isPrimes)


if __name__ == '__main__':
    n = 10
    print(countPrimes2(n))
