#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   FindSmallestLetterGreaterThanTarget.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/15 13:29   cecilia      1.0

题目描述：给定一个有序的字符数组 letters 和一个字符 target，要求找出 letters 中大于 target 的最小字符，如果找不到就返回第 1 个字符。
Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
"""


def findSmallestLetterGreaterThanTarget(letters, target) -> str:
    """
    寻找大于给定元素的最小元素
    :param letters:给定的字符
    :param target:目标字符
    :return:
    """
    l = 0
    h = len(letters) - 1

    while l <= h:
        mid = int(l + (h - l) / 2)
        if letters[mid] <= target:  # 如果中间的字符比目标字符要小，那么需要在右区间[m,h]继续寻找
            l = mid + 1
        else:
            h = mid - 1
    # 如果都没有找到，则返回第一个字符
    if l < len(letters):
        return letters[l]
    else:
        return letters[0]


if __name__ == '__main__':
    print(findSmallestLetterGreaterThanTarget(letters=['a', 'b', 'd'], target='f'))
