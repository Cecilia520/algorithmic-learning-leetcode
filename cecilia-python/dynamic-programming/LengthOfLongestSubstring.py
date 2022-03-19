#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   LengthOfLongestSubstring.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/14 12:41   cecilia      1.0        无重复字符的最长字串
问题描述：
给定一个字符串，计算字符串中无重复字符的最长字串的长度
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

示例：
输入：s='abcc'
输出：length=3

思路分析：
一、可以采用动态规划的思路——
先查找当前的字符串的无重复字符的长度，然后每次添加下一个新得字符，递归判断是否是最长的
二、窗口滑动
遍历字符，利用一个窗口保存当前遍历的字符串，如果发现当前的字符不在当前的窗口中，则窗口长度+1，
如果发现当前字符在当前的窗口中，那么移除该字符，更新当前的窗口长度，最后比较每次的当前的窗口长度，返回最大的长度即可
"""


def lengthOfLongestSubstring(s) -> int:
    """
    计算无重复最长字串的长度
    :param s:
    :return:
    """
    if len(s) == 1:
        return 1
    if s == '':
        return 0

    def findlengthOfSubString(s, i):
        """
        判断新增当前位置i的字符后的无重复字符的长度
        :param s:
        :param i:
        :return:
        """
        tmp_str = s[i]
        j = i - 1
        while j >= 0 and s[j] not in tmp_str:
            tmp_str += s[j]
            j -= 1
        return len(tmp_str)

    maxLength = 0
    for i in range(len(s)):
        maxLength = max(maxLength, findlengthOfSubString(s, i))
    return maxLength
