#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   IsSubsequence.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/7 14:32   cecilia      1.0        判断是否是子序列
问题描述：
问题描述：
    给定字符串s和t，判断s是否是t的子序列。s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例1：
s = "abc", t = "ahbgdc"
返回 true.

示例2：
s = "axc", t = "ahbgdc"
返回false.

后续挑战 :
    如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？
"""
def isSubsequence(s, t) -> bool:
    """
    判断是否是子序列
    解决方案一：遍历法（双指针）
    :param s:
    :param t:
    :return:
    算法分析：时间复杂度O(N^2),空间复杂度O(1)
    """
    si = 0
    ti = 0

    if len(s) == 0:
        return True
    elif len(t) == 0:
        return False
    while ti < len(t) and si < len(s):
        if s[si] == t[ti]:
            ti += 1
            si += 1
        else:
            ti += 1
    # 根据最后遍历子字符串s的长度和总长度是否相等，如果相等，那么说明是子字符串
    return si == len(s)


if __name__ == '__main__':
    s = "acb"
    t = "ahbgdc"
    print(isSubsequence(s, t))



