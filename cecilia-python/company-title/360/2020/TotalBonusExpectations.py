#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   TotalBonusExpectations.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/30 22:40   cecilia      1.0       总奖金的期望
问题描述：
西西是某公司的一名员工，该公司目前正在做的项目还有N天截止。为鼓励员工加班，在这N天内该公司每天都会为当天加班的员工发放奖金。
具体来说，对于当天加班的某位员工，如果该员工已经连续加班了i天(1<=i<=N),则其当天能获得的奖金为i（例如，第一天加班，则此时记为连续加班1天，获得奖金为1）.
西西制定了这N天内的加班计划，他每天要么加班，要么不加班，要么不确定加不加班（有50%的概率加班，剩下的50%不加班），那么西西在这N天内能获得的总奖金的期望是多少？

示例：
> 输入：
> 第一行包含一个整数，1<=N<=10000
> 第二行包含N个空格隔开的整数t1到tN,0<=ti<=2.
> 若ti=0，则表示西西在第i天不加班；
> 若ti=1，则表示西西在第i天会加班；
> 若ti=2,则表示西西在第i天有50%的概率加班，剩下的50%的概率不加班。

> 输出：总奖金的期望，结果保留整数部分。

思路分析：考察E=x1*p1+x2*p2+x3*p3+......xn*pn
"""


def getTotalBonusExpectations(nums):
    """
    求奖金总期望
    :param N:
    :param nums:
    :return:
    """
    if not nums:
        return 0

    overtime = unovertime = 0.5

    def isOvertime(overtime_flag, nums):

        N = len(nums)

        result = [0 for _ in range(N)]

        if nums[0] == 1:
            result[0] = 1
        elif nums[0] == 0:
            result[0] = 0
        elif nums[0] == 2:
            if overtime_flag == 0:  # 不加班
                result[0] = 0
            else:
                result[0] = 1

        for i in range(1, N):
            if nums[i] == 2:
                if overtime_flag == 1:
                    result[i] = result[i - 1] + 1
                if overtime_flag == 0:
                    result[i] = 0
            elif nums[i] == 1:
                result[i] = result[i - 1] + 1
            elif nums[i] == 0:
                result[i] = 0
        return result

    result = isOvertime(1, nums)  # 加班
    print("overtime_flag==1：{}".format(result))
    un_result = isOvertime(0, nums)  # 不加班
    print("overtime_flag!=1：{}".format(un_result))

    return sum(result) * overtime + sum(un_result) * unovertime


if __name__ == '__main__':
    print(getTotalBonusExpectations(nums=[1, 2, 1]))
