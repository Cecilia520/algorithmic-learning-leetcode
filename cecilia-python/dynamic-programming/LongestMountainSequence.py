#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   LongestMountainSequence.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/28 12:54   cecilia      1.0        最长连续山峰子序列（实质上最长连续子序列的衍变）
问题描述：给了一个序列，让找出最长的“凸子序列”
何为“凸子序列”：数列中有一个xi,使得所有x0<x1<x2….xi-1<xi且xi>xi+1>xi+1>….>xn
eg：12345431,是山峰序列，12345234不是山峰序列
注：单调递增或单调递减序列也算山峰序列；
单独一个数是长度为1的山峰序列

示例1
输入
[1,2,3,6,1]

输出
5

示例2
输入
[1,2,2,1]

输出
3
说明
1,2,1
"""


class Solution:
    def __init__(self):
        self.res = 0

    def getLongestMountainSequence(self, nums):
        """
        寻找最长连续山峰子序列
        问题分析：实质上该问题可以分解成最长连续上升子序列和最长连续下降子序列
        假设dp[flag][i]表示第i个数结尾的最大山峰子序列。
        当falg=0时，dp[0][i]=max(dp[0][p]) +1，其中p属于[0,i-1] 且nums[i]>nums[p],表示最长连续上升子序列；
        当flag=1时，dp[1][i]=max(dp[0][q],dp[0][q])+1，其中q属于[0,i-1] 且nums[i]<nums[p]
        :param nums:
        :return:
        算法分析：时间复杂度O(nm),空间复杂度O(n)
        """
        n = len(nums)
        if n == 1:
            return 1
        dp = [[0 for _ in range(n)] for _ in range(2)]

        dp[0][0] = 1
        dp[1][0] = 1

        for i in range(1, n):
            max0 = 0
            max1 = 0
            for j in range(i):
                if nums[i] > nums[j]:  # 上升，flag=0
                    max0 = max(max0, dp[0][j])
                elif nums[i] < nums[j]:
                    max1 = max(max1, dp[0][j], dp[1][j])
            dp[0][i] = max0 + 1
            dp[1][i] = max1 + 1

            self.res = max(self.res, dp[0][i], dp[1][i])  # 每一轮保存最大值
        return self.res


if __name__ == '__main__':
    nums = list(map(int, input().strip()[1:-1].split(",")))
    print(nums)
    s = Solution()
    res = s.getLongestMountainSequence(nums=nums)
    print(res)
