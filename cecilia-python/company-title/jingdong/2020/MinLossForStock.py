#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MinLossForStock.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/18 22:25   cecilia      1.0        股票最小亏损问题
问题描述：
最近经济不景气，小A准备将持仓的股票抛售一部分，他共持有n支股票，由于受平台的限制，他每天
最多只能卖出m支股票，已知第i支股票每天会亏损a_i元，即如果第k天抛售出这支股票，亏损的金额是k*a_i元。
现在他还没有决定具体卖出多少支股票，所以他会给你若干个询问，即如果卖出q支股票，这q支股票最少的亏损数额是多少元呢？

输入：第一行包含两个正整数n和m，表示小A持仓的股票数和每天最多能卖出的股票数量。（1<=a_i<=10000）;
第二行包含n个正整数，第i个数a_i表示第i支股票每天的亏损金额。
接下来一行有一个正整数Q，表示询问数量；
之后有Q行，每行有一个正整数q，表示假如卖出q支股票，最少的亏损金额是多少元呢？（q<=n）

>> 输入：
5 2
1 2 3 4 5
2
3
5
>> 输出：
7
22

解释：
一共有5支股票，每天最多可以抛售2支；
q=2，即有两个询问；
第一个询问，需要抛售3支股票，当选择第1，2，3号股票的时候损失最小。其中第一天抛售
2，3号股票，损失为5元；第二天抛售1号股票，损失为2*1元，最后和几位7元；
第二个询问5，需要抛售1，2，3，4，5号股票，其中第一天抛售4，5号股票，损失为9元；
第二天抛售2，3号股票，损失为2*2+2*3=10；
第三天抛售1号股票，损失为3*1元，总合计22元。
"""
import math


class Solution:
    def solution(self, n, m, nums, Q):
        """
        根据每个询问计算最少的损失
        :param n: 持仓的股票数量
        :param m:每天最多可以卖出去的股票数量
        :param nums:股票亏损的价格
        :param Q:每个询问中需要抛售的股票数量
        :return:
        """
        k = math.ceil(Q / m)  # 总共需要卖的天数

        nums = sorted(nums)

        dp = [0 for _ in range(k)]

        if k > 1:
            dp[0] = sum(nums[Q - m:Q])
        else:
            dp[0] = sum(nums[0:Q])

        i = 1

        if k > 1:
            end = Q - m
            start = end - m
            if start < 0:
                start = 0
            while i < k:
                dp[i] = dp[i - 1] + (i + 1) * (sum(nums[start:end]))
                end = end - m
                start = end - m
                if start < 0:
                    start = 0
                i += 1
        return dp[-1]


if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    q_num = int(input())  # 询问的数量
    Q = []
    s = Solution()
    for _ in range(q_num):
        Q = int(input())
        res = s.solution(n, m, nums, Q)
        print(res)
