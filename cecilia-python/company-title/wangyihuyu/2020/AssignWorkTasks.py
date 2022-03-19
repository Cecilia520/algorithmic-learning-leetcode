#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   AssignWorkTasks.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/19 18:12   cecilia      1.0       工作任务分配
问题描述：
厂长阿雄每天需要根据每天的劳动技能等级来给每个员工分配工作任务。
一个工作任务只能由劳动等级大于等于该任务难度的员工来完成，且同一天里一个员工
只能对应一个工作任务，一个工作任务只能由一个员工来完成。
员工i的劳动技能等级由整数Wi来表示，工作任务i的任务的难度由整数Ti表示。
请你帮助阿雄分配今天的工作任务？

输入描述：第一行输入员工数N，且1<N<100000;
第二行输入N个员工的劳动技能等级W，以空格分隔，1<Wi<10e9;
第三行输入N个任务的任务难度Ti，以空格分割，1<Ti<10e9;
第四行输入一个整数M，且1<M<10e9

输出描述：输出一个整数，该整数为所有可能的分配方式的数量除以M后的所得的余数。

示例1：
输入：
6
1 6 3 4 5 2
2 3 1 4 6 5
10

输出：1

示例2：
输入：
3
6 6 6
2 2 2
10

输出：6
"""