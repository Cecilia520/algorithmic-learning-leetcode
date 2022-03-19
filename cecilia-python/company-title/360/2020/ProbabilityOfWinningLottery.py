#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ProbabilityOfWinningLottery.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/30 22:26   cecilia      1.0        抽奖中奖的概率计算
问题描述：
A和B两个轮流抽奖。现在有一个抽奖箱，里面有n张中奖票，m张不中奖票。A和B轮流从中抽一张奖票出来。如果有人抽到中奖票就结束，抽到中奖概率的人胜利。抽到的奖票会被丢弃。
额外的，B每次抽到后，会再次抽取一张票并丢弃（这张票中奖不算B胜利）。
现在，A先抽，请问A的胜率，保留4位小数后输出。如果两个人到最后也没有抽到中奖票，算B胜利。

示例1：
> 输入：
> 2 3 分别代表中奖和不中奖的数量（n>=0,m<=100）
> 0.6000

示例2：
> 输入：1 3
> 0.5000
> 解释：
> 如果A第一轮抽到中将票，A胜利，概率0.25；
> 如果A第二轮抽到中奖票，情况位A第一轮没有抽到中将票，B也没有抽到中将票，并且B丢弃的奖票也不是中将票。概率为：
> 3/4 * 2/3 * 1/2 = 0.25
> 综上所述：0.25+0.25 = 0.5000
"""
import math

def award(n: int, m: int) -> float:
    """
    计算中奖的概率
    :param n:中奖的票数
    :param m:不中奖的票数
    :return:
    """
    total_times = math.ceil((n + m) / 3)
    n1, m1 = n, m
    n2, m2 = n, m
    probability = n / (m + n)

    # A和B都没有中奖，直到最后结束
    for i in range(1, total_times):
        probability = probability + (m1 / (m1 + n1)) * ((m1 - 1) / (m1 + n1 - 1)) * ((m1 - 2) / (m1 + n1 - 2))
        m1 = m1 - 3

    # A第一轮没有抽到，第二轮B也没有抽到，第三轮A抽到了中奖
    for i in range(1, total_times):
        probability = probability + (m2 / (m2 + n2)) * ((m2 - 1) / (m2 + n2 - 1)) * ((n2 - 1) / (m2 + n2 - 2))
        m1 = m1 - 2
        n2 = n2 - 1
    return probability


if __name__ == '__main__':
    print(award(2, 3))
