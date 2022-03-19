#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   RobMaxMoney-II.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/6 22:01   cecilia      1.0         小偷偷的最大金额-II
问题描述：
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。
这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。
同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2:

输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


def rob(nums: List[int]) -> int:
    """
    计算小偷偷的最大金额-II
    思路分析：和上一个题目相比，这个是环状排列，所以可以看出只能从第一家或者最后一家选一个行窃
    :param nums:
    :return:
    算法分析：时间复杂度O(n),空间复杂度O(1)
    """
    if not nums or len(nums) <= 0:
        return 0
    if len(nums) == 1:
        return nums[0]

    n = len(nums)

    def robNums(nums):
        dp_pre = 0
        dp_cur = 0
        for num in nums:
            dp_pre, dp_cur = dp_cur, max(dp_pre + num, dp_cur)
        return dp_cur

    # 不偷第一个或者不偷最后一个
    return max(robNums(nums[:n-1]), robNums(nums[1:]))


if __name__ == '__main__':
    print(rob(nums=[1, 2, 3, 1]))
