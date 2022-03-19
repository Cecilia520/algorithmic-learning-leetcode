#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MeetingScheduler-1229.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/12 11:26   cecilia      1.0       会议安排（leetcode第1229道题）——微软面试出现过
问题描述：
你是一名行政助理，手里有两位客户的空闲时间表：slots1 和 slots2，以及会议的预计持续时间 duration，请你为他们安排合适的会议时间。

「会议时间」是两位客户都有空参加，并且持续时间能够满足预计时间 duration 的 最早的时间间隔。

如果没有满足要求的会议时间，就请返回一个 空数组。

「空闲时间」的格式是 [start, end]，由开始时间 start 和结束时间 end 组成，表示从 start 开始，到 end 结束。

题目保证数据有效：同一个人的空闲时间不会出现交叠的情况，也就是说，对于同一个人的两个空闲时间 [start1, end1] 和 [start2, end2]，要么 start1 > end2，要么 start2 > end1。

示例：
输入：slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
输出：[60,68]

"""


def meetingScheduler(slots1, slots2, duration):
    """
    安排会议
    思路分析：寻找区间交集的最大间隔能否在会议要求的时间内
    :param slots1:空闲时间表1,[[]]
    :param slots2:空闲时间表2, [[]]
    :param duration:会议的容忍时间
    :return:返回符合要求的时间段, list([])
    算法分析：时间复杂度O(N+M),空间复杂度O(N+M)
    """
    # 首先将其进行排序
    slots1.sort()
    slots2.sort()

    # 然后使用双指针分别遍历
    i, j = 0, 0
    while i < len(slots1) and j < len(slots2):
        l = max(slots1[i][0], slots2[j][0])  # 确定空闲时间表中开始时间的最大时间
        r = min(slots1[i][1], slots2[j][1])  # 确定空闲时间表中结束时间最早的时间
        if l + duration <= r:
            return [l, l + duration]

        # 比较结束时间，如果当前客户的结束时间比第二个客户当前空闲时间结束时间要早，寻找第一个客户的下一个空闲时间
        if slots1[i][1] < slots2[j][1]:
            i += 1
        else:
            j += 1


if __name__ == '__main__':
    print(meetingScheduler(slots1=[[10, 50], [60, 120], [140, 210]],
                           slots2=[[0, 15], [60, 70]], duration=8))
