#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MaxStringIntervals.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/18 15:03   cecilia      1.0       最长字符区间
问题描述：链接：https://www.nowcoder.com/questionTerminal/43077cbb88024b2188de64a471352b8e
来源：牛客网

拉齐有一个01序列，他可以对这个序列进行任意多次变换，每次变换都是把序列的最后若干个元素放到最前面，例如：010011，将最后3个元素011放到最前面，序列变为011010。所有变换结束后，拉齐需要挑出一个全为1的连续区间，要求最大化区间长度。


输入描述:
共一行，一个01串，仅包含0或1。序列长度不超过50000。


输出描述:
一个整数，表示最长区间的长度。
示例1
输入
11011
输出
4

"""
import sys


class Solution:
    def getMaxStringIntervals(self, s: str) -> int:
        """
        获得最长字符区间
        思路：可以将字符串进行复制一遍放一起，利用双指针的方法进行遍历获得
        :param s:
        :return:
        """
        # 判断全是1或者全0的情况
        if s == '1' * len(s):
            return len(s)

        if s == '0' * len(s):
            return 0

        max_intervals = 0
        s = 2 * s
        n = len(s)
        i, j = 0, 0
        while i < n:
            while i < n and s[i] == '1':
                i += 1
            max_intervals = max(max_intervals, i - j)
            i += 1
            j = i
        return max_intervals


if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    solution = Solution()
    max_intervals = solution.getMaxStringIntervals(s=s)
    print(max_intervals)
