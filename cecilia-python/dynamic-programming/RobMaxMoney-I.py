#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   RobMaxMoney-I.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/6 22:00   cecilia      1.0         偷的最大金额
问题描述：
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:

输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
from typing import List


def rob(nums: List[int]) -> int:
    """
    计算小偷偷的最大金额
    思路分析：单排排列。状态转移很简单，寻找前一个和后一个最大
    dp[i] = max(dp[i-1] + nums[i], dp[i])
    :param nums:
    :return:
    算法分析：时间复杂度O(n),空间复杂度O(1)
    """
    if not nums or len(nums) <= 0:
        return 0
    if len(nums) == 0:
        return nums[0]
    n = len(nums)

    # 定义状态
    dp_pre = nums[0]
    dp_cur = max(dp_pre, nums[1])

    for i in range(2, n):
        dp_pre, dp_cur = dp_cur, max(dp_pre+nums[i], dp_cur)

    return dp_cur


if __name__ == '__main__':
    print(rob(nums=[1, 2, 3, 1]))
