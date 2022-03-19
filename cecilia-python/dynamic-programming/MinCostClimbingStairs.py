#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MinCostClimbingStairs.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/27 15:06   cecilia      1.0        使用最小花费进行爬楼梯
问题描述：数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。

每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

示例 1:

输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
 示例 2:

输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-cost-climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    """
    最小花费爬楼梯
    思路分析：明显一看就是动态规划求取最优子结构问题。
    首先确定动态转移状态,，在这个问题中，主要包括走一步楼梯和走两步两个状态，即递推关系：
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i](i>2);
        可以设定一个动态转移数组存储每步的cost，次选取最小花费的方式行走，经过多次逐步累积后，最后的解结构必定是最优的子结构。
        即所有的子结构的解集合{P1,P2,P3,P4.....Pn}，如果{P2,P3,P4,....Pn}是最优的，那么{P1,P2,P3,P4....Pn}一定是最优的。
    :param cost:
    :return:
    """
    # 判断边界情况
    if not cost or len(cost) < 0:
        return 0

    L = len(cost)

    # 状态转移数组
    dp = [0 for _ in range(L)]

    for c in cost:
        dp[1], dp[2] = min(dp[1], dp[2]) + c, dp[1]
        print(dp)

    return min(dp[1], dp[2])

if __name__ == '__main__':
    print(minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
    print(minCostClimbingStairs(cost=[0, 0, 0, 0]))
