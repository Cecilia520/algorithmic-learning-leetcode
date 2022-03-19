#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   CanTwoPartition.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/1 15:18   cecilia      1.0        是否能分割成两个和相等的子集（实质是0-1背包问题）
问题描述：
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:
每个数组中的元素不会超过 100
数组的大小不会超过 200

示例 1:
输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def canTwoPartition(nums):
    """
    是否能分割成两个和相等的子集
    思路分析：这问题实际上属于0-1背包问题，典型的动态规划问题。
    1. 确定转移状态。dp[i][j]定义为从[0,i]子区间内挑选一些正整数，每个数只能用一次，使得这些数的和能够是j
    2. 状态转移方程。 如果nums[i]=j,那么dp[i][j]=True; 如果nums[i]<j,那么dp[i][j] = dp[i][j] or dp[i][j-nums[i]]
    3. 初始化。对于dp[0][0] = false,而dp[0][1]取决于j是否等于num[0]
    4. 输出。dp[len(nums)-1][target]
    :param nums:
    :return:
    算法分析：时间复杂度O(NC),空间复杂度O(NC),N代表[0,i]的区间长度，C代表[0,C]的区间长度
    """
    if not nums or len(nums) == 0:
        return False

    n = len(nums)

    # 求所有的和
    all_nums = sum(nums)

    # 如果是奇数，则不满足，需要分割的是两个相等和的子集，说明和一定是偶数
    if (all_nums & 1) == 1:
        return False

    target = all_nums // 2

    dp = [[True for _ in range(target + 1)] for _ in range(n)]

    for i in range(1, n):
        for j in range(target + 1):
            # 直接从上一行先把结果抄下来，然后再修正
            dp[i][j] = dp[i - 1][j]

            if nums[i] == j:
                dp[i][j] = True
                continue

            if nums[i] < j:
                dp[i][j] = dp[i][j] or dp[i][j - nums[i]]

    return dp[n - 1][target]


def canTwoPartitionPlus(nums):
    """
    是否能切割成两个和相等的子集
    动态规划优化——状态压缩，减少空间，二维变成一维,将原来的[0,i]区间的容量为j的数组转变成直接将前i个物品组合放进容量为c的背包里，得到的最大的价值
    :return:
    """
    n = len(nums)

    if not nums or n <= 0:
        return False

    all_sum = sum(nums)

    # 奇数不符合
    if (all_sum & 1) == 1:
        return False

    target = all_sum // 2

    dp = [nums[0] if j >= nums[0] else 0 for j in range(target + 1)]

    for i in range(1, n):
        j = target
        while j > 0:
            if nums[i] <= j:
                dp[j] = max(dp[j], (nums[i] + dp[j - nums[i]]))
            else:
                break
            j -= 1
        if dp[j] == target:
            return True
    return True if dp[target] == target else False


if __name__ == '__main__':
    print(canTwoPartitionPlus(nums=[1, 5, 11, 5]))
