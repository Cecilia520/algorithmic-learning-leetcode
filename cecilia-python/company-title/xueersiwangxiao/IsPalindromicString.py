#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   LongestLengthPalindromicString.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/13 20:16   cecilia      1.0        判断一个字符串是否字符串
问题描述：给定一个字符串，判断是否是回文字符串，空字符判定为是回文字符串
其中可能存在一些无效的字符。
示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
"""
class Solution:
    def isPalindromicString(self,s):
        """
        判断是否是回文字符串
        思路：双指针
        :param s:
        :return:
        """
        # 考虑空字符,判定为是回文字符串
        if s == '':
            return True

        i, j = 0, len(s)-1
        while i < j:
            pass