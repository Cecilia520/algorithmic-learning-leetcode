#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   StreamMedium1.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/9/15 16:25   cecilia      1.0         None
"""
import heapq
import random


class FindMedium(object):

    def __init__(self):
        # 里面的元素都是正的, 故堆顶最大
        self.max_heap = []
        # 里面的元素都是负的，故堆顶的相反数最小
        self.min_heap = []
        self.item_count = 0

    def add_num(self, num: float):
        self.item_count += 1
        if self.item_count & 1 == 1:
            # 奇数的时候先将数据先放入大顶堆，然后取大顶堆的堆顶放入小顶堆
            heapq.heappush(self.max_heap, num)
            heap_top = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -heap_top)
            # 操作之后的效果就是：小顶堆的元素加一个
        else:
            # 偶数的时候先将数据放入小顶堆，然后取小顶堆的堆顶元素放入大顶堆
            heapq.heappush(self.min_heap, -num)
            heap_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -heap_top)
            # 操作之后的效果就是：大顶堆的元素加一个
        #

    def find_med(self):
        # 小顶堆堆大顶堆的所有元素都比小顶堆的元素的相反数小，且小顶堆的元素个数多于大顶堆一个或者相等顶元素的相反数就是中位数
        return -self.min_heap[0]


def auto_gen():
    times = int(input("Times:"))
    fm = FindMedium()
    nums = []
    rand = random.Random()
    for i in range(times):
        ram_int = rand.randint(0, 100)
        fm.add_num(ram_int)
        nums.append(ram_int)
        nums.sort()
        print(nums)
        print("find_med: {}".format(fm.find_med()))
        print("medium: {}".format(nums[len(nums) // 2 - 1] if len(nums) & 1 == 0 else nums[len(nums) // 2]))


def manual():
    fm = FindMedium()
    times = int(input("Times:"))
    for i in range(times):
        num = float(input("Num{}:".format(i + 1)))
        fm.add_num(num)
        print(fm.find_med())


if __name__ == '__main__':
    auto_gen()
    # manual()
