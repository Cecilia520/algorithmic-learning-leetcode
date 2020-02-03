#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ValidPalindrome.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/16 14:35   cecilia      1.0       回文字符串
题目描述：可以删除一个字符，判断是否是回文字符串
输入: "abca"
输出: True
解释: 你可以删除c字符。
"""


def validPalindrome(s: str) -> bool:
    """
    可删除一个字符串，判断是回文字符串
    :param str:
    :return:
    解题思路：使用双指针，分别从头和从尾部进行索引判断是否相等。
    如果出现不相等的情况，需要考虑是切割左指针处的数据还是切割右指针的数据进行对子字符串继续判断，
    由此看来，其中涉及到一个循环，刚开始对整个字符串进行执行判断是否使回文，然后出现不相等的情况时，
    又需要对子字符串进行再次判断是否是回文。
    主要思路:第一种：根据回文数的特点，直接进行循环判断
    算法分析：时间复杂度O(N), 空间复杂度O(1)
    """
    # 第一种：直接法
    if s == s[::-1]:  # 根据字符串自身反转判断是否相等，回文数经过反转后仍然能够和自身相等
        return True
    i, j = 0, len(s) - 1
    while i <= j:
        if s[i] == s[j]:
            i = i + 1
            j = j - 1
        else:
            # 获得子字符串
            a = s[i + 1: j + 1] # 要记得索引切片的时候，含前不含后
            print("a:{}".format(a))
            b = s[i:j]
            print("b:{}".format(b))
            return a == a[::-1] or b == b[::-1]


def validPalindrome2(s: str) -> bool:
    """
    可删除一个字符串，判断是回文字符串_贪心法
    :param str:
    :return:
    解题思路：使用双指针，分别从头和从尾部进行索引判断是否相等。
    如果出现不相等的情况，需要考虑是切割左指针处的数据还是切割右指针的数据进行对子字符串继续判断，
    由此看来，其中涉及到一个循环，刚开始对整个字符串进行执行判断是否使回文，然后出现不相等的情况时，
    又需要对子字符串进行再次判断是否是回文。
    主要思路: 第二种：贪心法
    算法分析：时间复杂度O(N^2), 空间复杂度O(N)
    """
    # 第一种：贪心法
    slist = list(s)
    i, j = 0, len(s) - 1
    if slist == slist[::-1]:
        return True
    while i <= j:
        if slist[i] != slist[j]:
            i = i + 1
            j = j - 1
            print("i:{},j:{}".format(slist[i], slist[j]))
        else:
            # 继续判断子字符串是否是回文
            return isvalidPalindrome(s, i, j - 1) or isvalidPalindrome(s, i + 1, j)

def isvalidPalindrome(s, i, j) -> bool:
    """
    递归判断子字符串是否是回文
    :param s: 子字符串
    :param i: 左指针
    :param j: 右指针
    :return:
    """
    slist = list(s)
    while i <= j:
        if slist[i] == slist[j]:
            i = i + 1
            j = j - 1
            print("i:{},j:{}".format(slist[i], slist[j]))
        else:
            return False


if __name__ == '__main__':
    print(validPalindrome2("abcba"))
