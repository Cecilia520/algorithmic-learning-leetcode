#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ChickenFarmsProblems.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/30 21:49   cecilia      1.0        养鸡场统计小鸡问题
问题描述：可以参考note.md中第三道题目
小强有n个养鸡场，第i个养鸡场初始时有a[i]只小鸡，与其他养鸡场不同的是，小强的每个养鸡场每天都会增加k只小鸡，
为了维持养鸡场良好的生态环境，小强在每天结束的时候都会在数量最多的养鸡场里卖掉一半的小鸡，即若当前最多的养鸡场含有x只小鸡，
经过贩卖后，当前养鸡场会剩下[x/2]只小鸡，现在问你经过m天后，小强的n个养鸡场里面一共有多少只小鸡？

示例：
> 输入：
> 3 3 100
> 100 200 400

> 输出：925

"""
def getChickenFarmsProblems(m, n, k, a):
    """
    统计养鸡场的小鸡总数
    :param m: 天数
    :param n: 养鸡场的个数
    :param k: 每天小鸡的增加数
    :param a: 养鸡场初始小鸡个数
    :return:
    """
    list.sort(a)

    t = m * n * k - n * (k // 2) # 总的增加的数据和减少的数据差

    for i in range(n):
        a[-1] = a[-1] // 2 - (k // 2)
        temb = a[-1]
        for day in range(1, m):
            if a[m - 1 - day] > temb:
                a[m - day] = a[m - 1 - day]
                if m - 1 - day == 0:
                    a[m - 1 - day] = temb
            else:
                a[m - day] = temb
                break

    return sum(a) + t


if __name__ == '__main__':
    m = 3
    n = 3
    k = 100
    a = [100, 200, 400]
    print(getChickenFarmsProblems(m, n, k, a))
