#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MinDistance.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/24 22:43   cecilia      1.0         编辑距离
问题描述：
72. 编辑距离
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符


示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
"""


class Solution:
    def getMinDistance(self, word1, word2):
        """
        编辑最小距离
        :param word1:
        :param word2:
        :return:
        """
        n = len(word1)
        m = len(word2)
        if not word1 or not word2 or n < 0 or m < 0:
            return 0

        if m == 0 or n == 0:
            return m+n
        #dp[i][j]表示word1的前i个字符和word2的前j个字符进行编辑距离，即前i个字符的word1需要经过多少步才能转换成前就个字符的word2
        dp = [[0 for _ in range(m + 1)] for _ in range(n+1)]
        print(dp)

        # 初始化
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + 1

        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] + 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1] # 如果单词相同，则不变
                else:
                    dp[i][j] = min(dp[i-1][j-1], min(dp[i - 1][j], dp[i][j - 1])) + 1 # 如果单词不相同，那么需要考虑删除、插入、替换操作的次数
        print(dp)
        return dp[n][m]


if __name__ == '__main__':
    s = Solution()
    res = s.getMinDistance(word1="horse", word2="ros")
    print(res)
