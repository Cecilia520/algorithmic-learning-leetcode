#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MinLossForStockQuickSort.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/18 23:10   cecilia      1.0       快排解决最小损失
"""
import math
import sys
from typing import List


def partition(arr, low, high):
    i = low
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def get_loss_amt(loss_list: List[int], m: int, q: int):
    amt = 0
    k = 1
    for i in range(q - 1, -1, -1):
        loss = loss_list[i]
        amt = amt + loss * math.ceil(k / m)
        k = k + 1
    return amt


if __name__ == '__main__':
    n_m = sys.stdin.readline()
    n_m_split = list(map(int, n_m.split(" ")))
    n, m = n_m_split[0], n_m_split[1]
    a_i = sys.stdin.readline()
    a_i_split = list(map(int, a_i.split(" ")))
    quick_sort(a_i_split, 0, n - 1)
    Q = sys.stdin.readline()
    for i in range(int(Q)):
        q = int(sys.stdin.readline())
        print(get_loss_amt(a_i_split, m, q))
