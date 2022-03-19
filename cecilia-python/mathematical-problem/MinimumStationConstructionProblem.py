#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MinimumStationConstructionProblem.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/7 16:22   cecilia      1.0         最少车站建造问题
问题描述：
有10^8个村庄排在一条公路上，依次编号为0~10^8-1，相邻村庄距离为1，其中有n个村庄居住着牛牛，
居住着牛牛的村庄从小到大依次为a0~an-1，其中保证a0=0.
现在需要建设车站，有两个要求必须被满足：
1、每个有牛牛居住的村庄必须修建车站。
2、相邻车站的距离必须为1或为某个质数。
现给出n和a数组，求需要建设车站的最小数量。

示例1
输入
3,[0,7,11]
输出
4
说明
在0,7,8,11处建造车站，差值分别为7,1,3，符合要求

备注:
输入数据包含一个数n和一个长度为n的数组a，数组a的下标为0~n-1，保证a数组递增，且a0=0。
输出一个整数，表示答案。
1<=n<=1000，a数组中数值保证小于10^8

链接：https://www.nowcoder.com/questionTerminal/9fededa1b63a41798e5d43344d7bf216
来源：牛客网

思路:
根据题意，车站数最少是n，如果相邻两个车站的距离不是1或素数，就需要在中间插入一个或多个车站来使每个车站之间的距离都是1或素数，
也就是求把一个非素数分解为素数的个数，可以想到哥德巴赫猜想。
对每个车站之间的距离进行判断，如果不是1或素数，就需要进行分解。如果距离是偶数，那么最多只需要新增一个车站；如果是奇数，
最多需要新增两个车站，但也有只需要新增一个车站的例子，比如9=2+7和15=2+13。如果想把一个奇数分解为两个素数，
就必须是一个奇素数、一个偶素数，偶素数只有2，所以先判断一下-2之后能不能得到素数，如果能，只需要新增1个车站；
如果不能，那么由哥德巴赫猜想，-2之后的奇数也一定能分解成2个素数，所以需要新增 2个车站。
"""
import math
class Solution:
    def isPrime(self, num):
        """
        判断是否是质数
        :param num:
        :return:
        """
        flag = True
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                flag = False
        return flag

    def work(self, n, a):
        """
        计算最少车站建造问题
        :param n:
        :param a:
        :return:
        """
        # 经过看讨论区，才知道这道题考察的是哥德巴赫猜想
        alen = len(a)
        count = 1
        for i in range(1, alen):
            distance = a[i] - a[i - 1]  # 计算相邻村庄的距离
            if self.isPrime(distance):
                count += 1
            elif self.isPrime(distance - 2) or distance % 2 == 0:  # 本身是偶数，并且-2是质数
                count += 2
            else:
                count += 3
        return count