#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   FindMinArrowShots.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/5 12:37   cecilia      1.0        用最少数量的箭引爆气球
问题描述：
气球在一个水平数轴上摆放，可以重叠，飞镖垂直投向坐标轴，使得路径上的气球都被刺破。求解最小的投飞镖次数使所有气球都被刺破。
开始坐标总是小于结束坐标。平面内最多存在104个气球。
在坐标x处射出一支箭，若有一个气球的直径的开始和结束坐标为 x_start，x_end， 且满足  x_start ≤ x ≤ x_end，则该气球会被引爆。

示例1：
输入:
[[10,16], [2,8], [1,6], [7,12]]
输出:
2
解释:
对于该样例，我们可以在x = 6（射爆[2,8],[1,6]两个气球）和 x = 11（射爆另外两个气球）。

问题分析：
可以跟踪气球的结束坐标，若下个气球开始坐标在当前气球的结束坐标前，则我们可以用一支箭一起引爆；
若下个气球的开始坐标在当前气球的结束坐标后，则我们必须增加箭的数量。并跟踪下个气球的结束坐标。

算法思路：
    1.根据 x_end 将气球进行排序。
    2.初始化 first_end 为第一个气球结束的坐标 points[0][1]。
    3.初始化箭的数量 arrows = 1。
    4.遍历所有的气球：
        如果气球的开始坐标大于 first_end：
        则增加箭的数量。
        将 first_end 设置为当前气球的 x_end。
    5.返回 arrows。
"""


def findMinArrowShots(points) -> int:
    """
    解决方案：贪心算法——根据区间结尾
    和计算五重叠区间个数题型类似，唯一不同的是，当接触时也会发生爆破
    @param: points 点集合 [][]
    @return int
    算法分析：时间复杂度O(nlog(n)),空间复杂度O(1)
    """
    # 判断区间集合是否存在或者为空集
    if not points or len(points) <= 0:
        return 0
    # 排序
    sort_points = sorted(points, key=lambda point: point[1])

    # 遍历判断
    cnt = 1
    current = 0
    current_end = sort_points[current][1]  # 第一个点

    for point_start, point_end in sort_points:
        # 如果当前气球在另一个气球结束后开始，则可以用一支箭一起引爆；
        # 若当前气球的结束坐标在下个气球的开始坐标前，则必须增加箭的数量
        if current_end < point_start:
            cnt += 1  # 增加一支箭
            current_end = point_end  # 从当前点的结束点开始继续判断
    return cnt


if __name__ == '__main__':
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    print(findMinArrowShots(points))
