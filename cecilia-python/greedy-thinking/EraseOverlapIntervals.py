#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   EraseOverlapIntervals.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/5 12:03   cecilia      1.0         无重叠区间
题型描述：
给定一个区间的集合，找到需要移除区间的最小数量，使得剩余区间互不重叠
注意:
1.可以认为区间的终点总是大于它的起点。
2.区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。

示例1：
输入: [ [1,2], [2,3], [3,4], [1,3] ]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。

示例2：
输入: [ [1,2], [1,2], [1,2] ]
输出: 2
解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。

示例3：
输入: [ [1,2], [2,3] ]
输出: 0
解释: 你不需要移除任何区间，因为它们已经是无重叠的了。

问题分析：
贪心算法，按照起点排序：选择结尾最短的，后面才可能连接更多的区间（如果两个区间有重叠，应该保留结尾小的） 。
把问题转化为最多能保留多少个区间，使他们互不重复，则按照终点排序，每个区间的结尾很重要，结尾越小，则后面越有可能容纳更多的区间。
"""


def eraseOverlapIntervals(intervals) -> int:
    """
    解决方案：贪心算法
    思路分析：
    先跟区间的结尾对区间进行排序，按照升序的规则；
    然后判断每个区间是否与另一个区间相交，如果一个区间不想与x的end相交，那么它的start必须大于或者等于x的end。每次选取结尾最小的与后一个区间的开头对比判断是否重叠
    :param intervals: 重叠区间集合
    :return:
    算法分析：时间复杂度O(nlog(n)),排序需要O(nlog(n)) 的时间,空间复杂度O(1)
    """
    if not intervals or len(intervals) <= 1: #考虑[[]]的情形
        return 0
    # 先对区间集合进行排序
    sort_intervals = sorted(intervals, key=lambda x: x[1])
    print(sort_intervals)
    cnt = 1  # 至少有一个区间
    current = 0  # 当前的区间
    for i in range(1, len(sort_intervals)):
        if sort_intervals[i][0] >= sort_intervals[current][1]:  # 如果每个区间都大于或者等于当前区间的结尾，那么可以判断为相交有重叠部分
            cnt += 1
            current = i  # 从当前区间开始继续判断
    # 总的区间个数减去重叠区间个数，等于不重叠区间个数
    return len(sort_intervals) - cnt


if __name__ == '__main__':
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    intervals1 = [[]]
    intervals2 = [[1, 100], [11, 22], [1, 11], [2, 12]]
    print(eraseOverlapIntervals(intervals1))
