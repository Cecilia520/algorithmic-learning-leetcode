#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   LongestStringNote.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/30 22:09   cecilia      1.0       最长字符串音符统计
问题描述：
小强最近喜欢弹钢琴，一段旋律中的每个音符都可以用一个小写英文字母表示。
当组成一段段旋律的字符ASCII码是非递减的，旋律被称为是高昂的，例如aaa，bcd。
现在小强已经学会了n段高昂的旋律，他想利用他们拼接出一个尽可能长的高昂的旋律，问最长长度是多少？

输入描述：n行每行一个字符串，保证每个字符串中的字符的ASCII是非递减的。n在[1, 1000,000]，
保证所有字符串长度之和不超过1000,000且仅由小写字母构成。

示例1：
> Input：
4
aaa
bcd
zzz
bcdef

> OutPut:  11。将1，4，3段字符拼接在一起，长度为11。

示例2：
输入：
4
abghkl
behklmmm
hopqsttz
yzzz

输出：
12
"""


class Solution:
    def getMaxLongestNote(self, n, notes):
        """
        计算最长上升的音符串的拼接长度
        思路方法：双指针法。创建两个指针，一个指针指向当前的音符的首字母索引位置，一个指针指向前一个字符的末尾字符的索引位置。
        其实题目是给定了n个上升音符串，如果题目给定的音符不是满足上升非递减规律，另外还需要对每个音符串做判断的，
        但是这里已经说明了每个音符是满足非递减规律的，因此不需要考虑内部的，只需要考虑字符串之间的关系。
        :param n: 音符集合长度
        :param notes: 音符集合
        :return:
        算法分析：时间复杂度O(NlogN),空间复杂度O(N)
        """
        if n < 0:
            return 0

        # 对所有的字符集合中的首字母进行排序
        notes = sorted(notes)
        #
        print(notes)

        # 定义状态，dp[i]代表前i个音符组成的最长长度
        dp = [0] * n
        dp[0] = len(notes[0])

        maxL = 0
        maxres = 0
        curentL = 0
        for i in range(1, n):
            for j in range(i):
                # 如果当前音符的首字符大于前一个音符的末尾字符
                if notes[i][0] >= notes[j][-1]:
                    # curentL = len(notes[i]) + len(notes[j])
                    dp[i] = max(dp[j], len(notes[j]) + len(notes[i]))
            dp[i] = maxL + len(notes[i])
            maxres = max(maxres, dp[i])

        print(dp)
        return max(dp)


if __name__ == '__main__':
    n = int(input())
    notes = []
    for i in range(n):
        notes.append(input())
    # print(notes)

    s = Solution()
    res = s.getMaxLongestNote(n, notes)
    print(res)
