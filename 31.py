#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   31.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/18 10:38   cecilia      1.0       最优二叉树II
小团有一个由N个节点组成的二叉树，每个节点有一个权值。定义二叉树每条边的开销为其两端节点权值的乘积，二叉树的总开销即每条边的开销之和。小团按照二叉树的中序遍历依次记录下每个节点的权值，即他记录下了N个数，第 i 个数表示位于中序遍历第 i 个位置的节点的权值。之后由于某种原因，小团遗忘了二叉树的具体结构。在所有可能的二叉树中，总开销最小的二叉树被称为最优二叉树。现在，小团请小美求出最优二叉树的总开销。

例如：7 6 5 1 3

最优二叉树如图所示，总开销为7*1+6*5+5*1+1*3=45。

输入描述
第一行输入一个整数N（1<=N<=300），表示二叉树的节点数。

第二行输入N个由空格隔开的整数，表示按中序遍历记录下的各个节点的权值，所有权值均为不超过1000的正整数。

输出描述
输出一个整数，表示最优二叉树的总开销。


样例输入
5
7 6 5 1 3
样例输出
45
"""
"""
total,78
新网1号,5,2.0%
新网2号,12,2.5%
新网3号,16,2.8%
新网4号,17,2.9%
null
"""
import sys


class Solution:
    def getMaxProfie(self, total, xinwang_dict):
        """
        寻找最优的组合收益方式
        :param total:
        :param rate_dict:
        :return:
        """
        sorted(xinwang_dict.items(), key=lambda item: item[1], reverse=True)
        for k, v in xinwang_dict.items():
            profit_sum = 0
            profit_sum += v
            if profit_sum <= total:
                print(str(k) + ',', str(v))


if __name__ == '__main__':
    solution = Solution()
    total = int(input().strip().split(',')[1])
    xinwang_dict = {}
    while True:
        try:
            lines = sys.stdin.readline().strip()
            if lines == 'null':
                break
            name, money, rate = lines.split(',')
            money = int(money)
            rate = float(rate[:-2])
            profit = money * rate
            xinwang_dict[name] = profit
            print(xinwang_dict)
        except:
            # break
            exit(0)
    solution.getMaxProfie(total, xinwang_dict)
