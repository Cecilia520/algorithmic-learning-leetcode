#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   CoinChange.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/5 20:39   cecilia      1.0         零钱兑换
问题描述：
给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def coinChange(coins, amount) -> int:
    """
    零钱兑换，寻找零钱个数最少的组合
    思路分析：动态规划。
    1.状态数组，dp[n]表示凑齐amount零钱的最少个数；
    2.初始化；
    3.状态转移：dp[i] = min(dp[i], dp[i - coin]+1).如果我们有1，2，5元硬币，那么要凑出11元，那么很自然想到需要从dp[n-1],dp[n-2],dp[n-5]中找到最小的进行组合
    :param coins:
    :param amount:
    :return:
    算法分析：时间复杂度O(SN),S表示金额，n表示面额数，一共计算S个状态。每次需要遍历n个面额来转移状态；
    空间复杂度O(S),总金额amount+1的长度大小
    """
    if amount < 0:
        return -1
    if amount == 0:
        return 0
    if not coins:
        return -1

    # 定义状态数组
    dp = [amount + 1 for _ in range(amount + 1)]

    dp[0] = 0

    # 状态转移
    for i in range(amount + 1):
        # 遍历所有硬币
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] <= amount else -1


if __name__ == '__main__':
    print(coinChange(coins=[1, 2, 5], amount=11))
