#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   DailyTemperatures.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/7 22:11   cecilia      1.0        数组中元素与下一个比它大的元素之间的距离
问题描述：
根据每日 气温 列，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高超过该日的天数。
如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

"""
def dailyTemperatures(nums):
    """
    思路：单调栈
    :param nums:
    :return:
    """
    stack = []
    L = len(nums)
    dist = [0]*L

    for i in range(L):
        while stack and nums[i] > nums[stack[-1]]:
            dist[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)

    return dist

if __name__ == '__main__':
    print(dailyTemperatures(nums=[73, 74, 75, 71, 69, 72, 76, 73]))

