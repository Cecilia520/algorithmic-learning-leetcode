#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   LongestCommonSubsequence.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/27 16:43   cecilia      1.0        最长公共子序列（LCS问题）
问题描述：
给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

若这两个字符串没有公共子序列，则返回 0。

示例 1:

输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace"，它的长度为 3。
示例 2:

输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc"，它的长度为 3。
示例 3:

输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def longestCommonSubsequence(s1: str, s2: str) -> int:
    """
    最长公共子序列的长度
    思路分析：基本的常规思路，确定转移状态，首先是先第一个字符串中每个字符需要和第二个字符串中的每个进行比较，如果相等，说明存在公共字符，此时记录加1，否则继续遍历；
        1. 转移状态。此时确定状态转移就是每一步比较后的结果值，使用dp[i][j]进行存储每一步比较的结果值；
        2. 初始化。对于第一个字符串需要初始化第一个字符与第二个字符串中的每个字符进行比较后的结果值，如果相等，记录加1，否则等于上一个记录值，不加也不减；第二个字符串中的第一个字符也同理。
        3. 状态转移过程。
            对于s1[i]==s2[j],那么dp[i][j]=dp[i-1][j-1] + 1;
            对于s1[i]!=s2[j],那么dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    :param s1:
    :param s2:
    :return:
    算法分析：时间复杂度O(mn),空间复杂度O(n)
    """
    l1 = len(s1)
    l2 = len(s2)

    if l1 <= 0 or l2 <= 0:
        return 0

    dp = [[0 for _ in range(l2)] for _ in range(l1)]

    if s1[0] == s2[0]:
        dp[0][0] = 1
    else:
        dp[0][0] = 0

    # 初始化
    for i in range(1, l1):
        # 用字符串s1中的每个字符和s2中的第一个字符比较，相等填充1，不相等，延续上一个记录的值
        if s1[i] == s2[0]:
            dp[i][0] = 1
        else:
            dp[i][0] = dp[i - 1][0]

    for j in range(1, l2):
        # 用字符串s1中的第一个字符和s2中的字符进行比较，如果相等，填充1，不相等，延续上一个记录的值
        if s1[0] == s2[j]:
            dp[0][j] = 1
        else:
            dp[0][j] = dp[0][j - 1]

    for i in range(1, l1):
        for j in range(1, l2):
            # 每次内循环，s1[i]中的元素和s2中的每个字符都进行比较一次，相等，等于上次记录的值加1，否则取相邻哪个最大记录的值
            if s1[i] == s2[j]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[l1 - 1][l2 - 1]


def longestCommonSubsequencePlus(s1: str, s2: str) -> int:
    """
    优化版：动态规划表优化。
        在每个字符串的最前面添加空串，那么动态规划表的第一行和第一列都填充为0，因为空串和其他字符相比，都不相等。
    思路分析：这种问题属于动态规划问题，最关键在于定义状态函数，以及根据两个字符长度不同定义状态转移过程；
    1.状态函数定义：dp[i][j]表示A的前i个字符与B的前j个字符的最长公共字串的长度
    2.状态转移：如果A[i]==B[j],那么dp[i][j] = dp[i-1][j-1] + 1;否则，dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    其实对于长度不相等的情况中，可能存在A[i]和B[j]都不在最长公共子序列中，那么此时dp[i][j] = max(dp[i-1][j-1],dp[i-1][j], dp[i][j-1])
    其实，对于这个没有必要，因为dp[i-1][j-1]一定是三个中最短的，一定不会取到，因此可以不需要添加上
    :param s1:
    :param s2:
    :return:
    """
    if not s1 or len(s1) <= 0 or not s2 or len(s2) <= 0:
        return 0

    l1 = len(s1)
    l2 = len(s2)

    dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]

    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

            print(dp)

    return dp[l1][l2]



if __name__ == '__main__':
    print(longestCommonSubsequencePlus(s1='1A2C3D4B56', s2='B1D23CA45B6A'))
    # print(longestCommonSubsequencePlus(s1="aba", s2="dba"))
