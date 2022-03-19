#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MinDistance.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/28 17:58   cecilia      1.0        编辑距离（腾讯、快手都遇到过的题目——动态规划）
问题描述：
给定两个单词word1和word2，计算出word1转换成word2的最少操作数目。
可以对单词进行如下操作：
1.插入一个单词；
2.删除一个单词；
3.替换一个单词。

示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释:
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2:

输入: word1 = "intention", word2 = "execution"
输出: 5
解释:
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def minDinstance(word1: str, word2: str) -> int:
    """
    编辑最短距离
    思路分析：首先立马想到属于动态规划的问题，最重要的是找出动态转移方程。
        设定dp[i][j]当字符串 word1 的长度为 i，字符串 word2 的长度为 j 时，将 word1 转化为 word2 所使用的最少操作次数为 dp[i][j]。
        那么状态转移方程可以表示为：
            dp[i][j] = min(dp[i-1][j-1], min(dp[i][j-1], dp[i-1][j-1])) + 1
            1. 如果把word1[i]==word2[j],那么dp[i][j] = dp[i-1][j-1]+1;
            2. 如果在word1中插入一个字符使得两个字符串相等，那么dp[i][j] = dp[i][j-1] + 1;
            3. 如果在word1中删除一个字符使得两个字符相等，那么dp[i][j] = dp[i-1][j] + 1
        最优子结构需要满足问题的每个解都是独立的，那么问题可以转化成求解每一次操作后累积的最少次数。
    :param word1:
    :param word2:
    :return:
    算法分析：时间复杂度O(nm),空间复杂度O(nm)
    """
    m = len(word1)
    n = len(word2)

    print("m:{}, n:{}".format(m, n))

    # 判断边界条件，如果其中一个字符串是空串或者两个都是空串，那么返回的操作次数是两个长度之和
    if m == 0 or n == 0:
        return m + n

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # 初始化
    for i in range(1, m+1):
        dp[i][0] = dp[i - 1][0] + 1

    for j in range(1, n+1):
        dp[0][j] = dp[0][j - 1] + 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1])) + 1
        print(dp)

    return dp[m][n]


if __name__ == '__main__':
    # print(minDinstance(word1="intention", word2="execution"))
    # print(minDinstance(word1="", word2="e"))
    print(minDinstance(word1="distance", word2="springbok"))
