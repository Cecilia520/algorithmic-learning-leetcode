#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   StreamMedium.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/9/14 20:34   cecilia      1.0       数据流中的中位数（订单金额的中位数）
实时统计每日订单金额中的“中位数”
- 每个订单金额是一个2位小数的定点正数，且超过1000.00；
- 中位数指n个数按升序排列后；
 - 排在第（n+1）/2位的数，当n为奇数；
 - 排在第2/n位的数，当n为偶数；注意此处与一般统计意义上中位数不同

输入描述：
输入有n+1行
第一行输出整数n(n>=1)
后续n行，每行是一个订单金额

例子：
输入：
5
0.01
5.00
55.00
4.00
999.99

输出：
0.01
0.01
5.00
4.00
5.00

"""
import heapq
class FindMedium:
    def __init__(self):
        self.cnt = 0 #记录大顶堆和小顶堆的长度
        self.max_heap = []
        self.min_heap = []
    def addElement(self, num:float)->None:
        """
        从数据流中添加元素
        :param num:
        :return:
        """
        self.cnt += 1
        heapq.heappush(self.max_heap, (-num, num))
        max_heap_top = heapq.heappop(self.max_heap) # 获取最大堆的堆顶元素
        heapq.heappush(self.min_heap, max_heap_top) # 将大顶堆的堆顶元素加入小堆顶
        if self.cnt & 1:
            min_heap_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, (-min_heap_top, min_heap_top))

    def findMedian(self):
        return self.max_heap[0][1]

    def addElement2(self, num:float)->None:
        """
        第二种方法
        :param num:
        :return:
        """
        self.cnt += 1
        heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
        if self.cnt & 1:
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))


    def findMedian2(self):
        # if self.cnt & 1:
        #     return (self.min_heap[0] - self.max_heap[0]) / 2.0
        # return self.min_heap[0]
        return self.min_heap[0]

if __name__ == '__main__':
    fm = FindMedium()
    n = int(input()) # 输入的元素有几个
    # for i in range(n):
    #     num = float(input())
    #     fm.addElement(num=num)
    #     print(fm.findMedian())
    print("-------第二种思路------")
    for j in range(n):
        num = float(input())
        fm.addElement2(num=num)
        print(fm.findMedian2())