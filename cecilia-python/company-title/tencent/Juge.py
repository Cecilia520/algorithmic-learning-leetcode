#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   Juge.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/9/6 21:50   cecilia      1.0         None
"""
from typing import List


class Solution:
    def calAUC(self, prob, labels):
        f = list(zip(prob, labels))
        rank = [values2 for values1, values2 in sorted(f, key=lambda x: x[0])]
        ranknew = [(values1, values2) for values1, values2 in sorted(f, key=lambda x: x[0])]
        rankList = [i + 1 for i in range(len(rank)) if rank[i] == 1]
        print(f)
        print(rank)
        print(ranknew)
        print(rankList)
        posNum = 0
        negNum = 0
        for i in range(len  (labels)):
            if (labels[i] == 1):
                posNum += 1
            else:
                negNum += 1
        auc = 0
        auc = (sum(rankList) - (posNum * (posNum + 1)) / 2) / (posNum * negNum)
        print(auc)
        return auc


if __name__ == '__main__':
    s = Solution()
    print("print-1.....")
    label = [1, 0, 0, 0, 1, 0, 1, 0]
    prob = [0.9, 0.8, 0.3, 0.1, 0.4, 0.9, 0.66, 0.7]
    print(s.calAUC(prob, label))

    #
