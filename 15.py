#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   15.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/9/19 13:52   cecilia      1.0         None

输入：
5 3
1 2 3 4
5 1
1 1
5 3
输出：
4
0
2
"""
"""
思路：
每次查找需要运算k次，根据数据范围，时间复杂度为O(n^2),这种方法不合适，会超时，可以采取动态规划的思路将问题分解，
定义dp[i,j]表示第i个元素向上找2^j次后的元素结果
"""


class Solution:
    def getParent(self, nums, x, k):
        """
        获取k级的祖先
        @param nums
        @param x
        @param k
        """
        n = len(nums)
        if x == 1 and k == 1:
            return 0
        dp = [[0 for _ in range(16)] for _ in range(n)]  # 最大数据为50000，2^n >= 50000,那么n=16
        for i in range(n):
            dp[i][0] = nums[i]
        for j in range(1, 16):
            for i in range(n):
                if dp[i][0] != 0:
                    dp[i][j] = dp[dp[i][j - 1]][j - 1]
        for i in range(16):
            if k & (1 << i):
                if x > 0:
                    return dp[x][i]
                else:
                    return 0


if __name__ == '__main__':
    s = Solution()
    n, q = map(int, input().strip())
    parents = list(map(int, input().strip()))
    for i in range(q):
        x, k = map(int, input().strip())
        print(s.getParent(parents, x, k))
