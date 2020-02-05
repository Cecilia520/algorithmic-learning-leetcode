#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MaxProfit-Ⅰ.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/5 12:39   cecilia      1.0        买卖股票的最佳时机Ⅰ（简单）
问题描述：
给定一个数组，他的第i个元素是一支给定股票第i天的价格
如果你最多只能允许完成一笔交易（即买入卖出一支股票），设计一个算法来计算你所获得最大利润
注意：不能在买入股票前卖出股票

示例1：
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

示例2：
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

问题分析：
实际上问题可以转化为寻找数组中两个最大差值（即最大利润），并且第二个数字（卖出价格）必须比第一个数字大（买入价格）。
形式上，对于每组 i 和 j（其中 j > i）我们需要找出 max(prices[j] - prices[i])。

"""


def maxProfit(prices) -> int:
    """
    买卖股票的最佳时机Ⅰ
    解决方案一：最常规的思路就是遍历两次数组，最后的时间复杂度和肯定是O(n^2),这是不太理想的!
    :param prices: 股票价格数组
    :return:
    算法分析：时间复杂度O(n^2),空间复杂度O(1),只维护两个变量，最后检查超时！！！😖
    """
    maxprofit = 0  # 初始化最大利润
    # 循环价格数组
    for i in range(0, len(prices) - 1):
        for j in range(1, len(prices)):
            if j > i:
                profit = prices[j] - prices[i]
                # print(profit)
                if profit > maxprofit:
                    maxprofit = profit
    return maxprofit


def maxProfit1(prices) -> int:
    """
    解决方案二：峰谷法，峰就是最大利润，谷底就是差值最小的值。一次遍历，维护最小价格和最大利润
    :param prices:
    :return:
    """
    min_price = float('inf')
    maxprofit = 0
    for i in range(len(prices)):
        min_price = min(prices[i], min_price)
        maxprofit = max(maxProfit, prices[i] - min_price)
    return maxprofit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    # prices1 = [7, 6, 4, 3, 1]
    print(maxProfit1(prices))
