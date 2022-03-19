#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   26.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/14 20:11   cecilia      1.0         None
"""
from typing import List
import collections


class Solution:
    def get_solution(self, N: int, pockets: List[int]) -> str:
        """
        扑克牌分析
        :param N: 牌数
        :param pockets: 牌型
        :return:
        """
        results = ['HuangJiaTongHuaShun', 'TongHuaShun', 'SiTiao', 'HuLu', 'TongHua', 'ShunZi', 'SanTiao', 'LiangDui',
                   'YiDui', 'GaoPai']
        pocket_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        hua_se = 'SHCD'
        huase_dict = collections.defaultdict(list)
        pik_dict = collections.defaultdict(list)
        for i in pockets:
            huase_dict[i[0]].append(i[1:])
            pik_dict[i[1:]].append(i[0])
        res = [len(results) - 1]
        for item in hua_se:
            if len(huase_dict[item]) >= 5:
                res.append(4)
                tmp = [pocket_list.index(i) for i in huase_dict[item]]
                if 12 in tmp:
                    tmp.append(-1)
                tmp.sort(reverse=True)
                for i in range(len(tmp) - 4):
                    if tmp[i] - 4 == tmp[i + 4]:
                        if tmp[i] == 12:
                            res.append(0)
                        else:
                            res.append(1)
        for pocket in pocket_list:
            if len(pik_dict[pocket]) == 4:
                res.append(2)
            if len(pik_dict[pocket]) == 3:
                if 6 in res or 8 in res:
                    res.append(6)
            if len(pik_dict) == 2:
                if 6 in res:
                    res.append(3)
                if 8 in res:
                    res.append(7)
        pik_list = []
        for i in pik_dict:
            if pik_dict[i]:
                pik_list.append(pocket_list.index(i))
        if len(pik_list) >= 5:
            if 12 in pik_list:
                pik_list.append(-1)
            pik_list.sort(reverse=True)
            for i in range(len(pik_list) - 4):
                if pik_list[i] - 4 == pik_list[i + 4]:
                    res.append(5)
        return results[min(res)]


if __name__ == '__main__':
    s = Solution()
    N = int(input())
    pockets = input().strip().split()
    print(s.get_solution(N, pockets))
