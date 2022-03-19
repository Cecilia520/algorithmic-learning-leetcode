#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   LongestLengthPalindromicString.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/13 20:16   cecilia      1.0       最长回文字符串
问题描述：给定一个字符串s，找到字符串s的最长回文字符串
示例 1：
输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"
"""
class Solution:
    def getLongestPalindromicString(self, s):
        """
        判断一个字符串是否是回文字符串
        思路：动态规划思维
        :param str:
        :return:
        """
        n = len(s)

        if n == 1:
            return 0

        # 定义dp数组
        dp = [[0 for _ in range(n)]for _ in range(n)]

        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        print(dp)
        return dp[0][n-1]

if __name__ == '__main__':
    s = input()
    solution = Solution()
    print(solution.getLongestPalindromicString(s))