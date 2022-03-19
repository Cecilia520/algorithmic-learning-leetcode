#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   QuickSort.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/9/20 18:18   cecilia      1.0         None
"""


class QuickSort(object):

    def sort(self, array, l, r):
        if l < r:
            pivot = array[l]
            i, j = l, r
            while i < j:
                while j > i and array[j] > pivot:
                    j = j - 1
                if i < j:
                    array[i] = array[j]
                while i < j and array[i] <= pivot:
                    i = i + 1
                if i < j:
                    array[j] = array[i]
            array[i] = pivot
            self.sort(array, l, i)
            self.sort(array, i + 1, r)
        print(array)

    def quick_sort(self, array):
        self.sort(array, 0, len(array) - 1)


if __name__ == '__main__':
    array = [1, 4, 6, 9, 10, 2, 3, 5, 8, 7]
    qs = QuickSort()
    qs.quick_sort(array)
