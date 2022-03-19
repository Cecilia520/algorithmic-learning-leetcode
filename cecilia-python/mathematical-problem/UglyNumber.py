#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   UglyNumber.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/15 12:56   cecilia      1.0       丑数(动态规划题型)
问题描述：
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。
求按从小到大的顺序的第N个丑数。
"""


def getUglyNumber_Solution(index):
    """
    从小到大打印丑数（2018年滴滴和网易考到过）
    :param index:
    :return:
    """
    if index < 7:
        return index

    # 创建一个数组列表保存丑数
    res = [1]
    # 设定三个指针
    t2, t3, t5 = 0, 0, 0
    for i in range(1, index):
        res.append(min(res[t2] * 2, min(res[t3] * 3, res[t5] * 5)))
        if res[i] == res[t2] * 2:
            t2 += 1
        if res[i] == res[t3] * 3:
            t3 += 1
        if res[i] == res[t5] * 5:
            t5 += 1
    return res[index - 1]

if __name__ == '__main__':
    print(getUglyNumber_Solution(1500))