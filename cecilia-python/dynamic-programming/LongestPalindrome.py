#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   LongestPalindrome.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/23 23:00   cecilia      1.0       最长回文字串
问题描述：
给定一个字符串，判断是否是回文串，如果是，返回字串

思路分析：

"""


def longestPalindrome(s: str) -> str:
    """
    寻找最长回文子串
    :param s:
    :return:
    """
    L = len(s)
    # 最大字串长度和开始位置
    maxL = 1
    start = 0

    # 如果字符长度小于2
    if L < 2:
        return s
    # 定义一个转移状态
    dp = [[False for _ in range(L)] for _ in range(L)]
    # 设定对角线部位
    for i in range(L):
        dp[i][i] = True

    # 分情况讨论
    for j in range(1, L):
        for i in range(0, j):
            if s[i] == s[j]:
                if j - i < 3:  # j-1 - (i+1) < 2 == j-i<3
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = False

            # 记录字串是回文满足时的最大长度和开始位置
            if dp[i][j]:
                curL = j - i + 1
                if curL > maxL:
                    maxL = curL
                    start = i
    return s[start:start + maxL]

if __name__ == '__main__':
    print(longestPalindrome(s='babad'))
