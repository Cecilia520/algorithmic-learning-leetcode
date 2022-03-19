#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   29.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/18 10:29   cecilia      1.0       食堂用餐

小美和小团所在公司的食堂有N张餐桌，从左到右摆成一排，每张餐桌有2张餐椅供至多2人用餐，公司职员排队进入食堂用餐。

小美发现职员用餐的一个规律并告诉小团：当男职员进入食堂时，他会优先选择已经坐有1人的餐桌用餐，只有当每张餐桌要么空着要么坐满2人时，他才会考虑空着的餐桌；当女职员进入食堂时，她会优先选择未坐人的餐桌用餐，只有当每张餐桌都坐有至少1人时，她才会考虑已经坐有1人的餐桌；无论男女，当有多张餐桌供职员选择时，他会选择最靠左的餐桌用餐。

现在食堂内已有若干人在用餐，另外M个人正排队进入食堂，小团会根据小美告诉他的规律预测排队的每个人分别会坐哪张餐桌。

输入描述
第一行输入一个整数T（1<=T<=10），表示数据组数。

每组数据占四行，第一行输入一个整数N（1<=N<=500000）；

第二行输入一个长度为N且仅包含数字0、1、2的字符串，第i个数字表示左起第i张餐桌已坐有的用餐人数；

第三行输入一个整数M（1<=M<=2N且保证排队的每个人进入食堂时都有可供选择的餐桌）；

第四行输入一个长度为M且仅包含字母M、F的字符串，若第 i 个字母为M，则排在第 i 的人为男性，否则其为女性。

输出描述
每组数据输出占M行，第 i 行输出一个整数 j （1<=j<=N），表示排在第 i 的人将选择左起第 j 张餐桌用餐。


样例输入
1
5
01102
6
MFMMFF
样例输出
2
1
1
3
4
4
"""
class Solution:
    def get_solution(self, N, tables, M, queue):
        table_list = list(map(int, tables))
        for i in range(M):
            if "M" == queue[i]:
                one_index = -1 if 1 not in table_list else table_list.index(1)
                if one_index != -1:
                    table_list[one_index] += 1
                    print(one_index + 1)
                else:
                    zero_index = table_list.index(0)
                    table_list[zero_index] += 1
                    print(zero_index + 1)
            else:
                zero_index = -1 if 0 not in table_list else table_list.index(0)
                if zero_index != -1:
                    table_list[zero_index] += 1
                    print(zero_index + 1)
                else:
                    one_index = table_list.index(1)
                    table_list[one_index] += 1
                    print(one_index + 1)
if __name__ == '__main__':
    s = Solution()
    T = int(input().strip())
    for i in range(T):
        N = int(input().strip())
        tables = input().strip()
        M = int(input().strip())
        queue = input().strip()
        s.get_solution(N, tables, M, queue)
