#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MedianInDataStream.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/9 10:16   cecilia      1.0        数据流中的中位数
问题描述：
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例 1：

输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]
示例 2：

输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
'''
该题在面试中经常出现过，其解决方案也有多种，需要深刻理解思路和过程
第一，在看题目之前需要注意给定的数组是无序的，可以使用二分查找或者优先队列的方法

第二，如果给定的数组是有序的，那么题目稍微比较简单
'''
import bisect
from heapq import *


class Solution:
    def __init__(self):
        # 提供给二分查找的初始化变量
        self.store = []

        # 提供给优先队列的方法初始化的对象
        self.minHeaq = []  # 小顶堆
        self.maxHeaq = []  # 大顶堆

    def addElement(self, num):
        """
        添加流数据——》二分查找
        :param num:
        :return:
        """
        if not self.store:
            self.store.append(num)
        else:
            # 二分查找对应位置再插入
            bisect.insort_left(self.store, num)  # 二分查找插入

    def findMedianInDataStreamBinarySearch(self):
        """
        方法一：使用二分查找的方法查找中位数
        :return:
        复杂度分析：时间复杂度O(logN)+O(N)==O(N),空间复杂度O(N)
        """
        n = len(self.store)
        if n & 1 == 1:  # 如果当前数组长度为奇数，那么中位数等于中间的
            return self.store[n // 2]
        else:
            return (self.store[n // 2] + self.store[n // 2 - 1]) / 2

    def addNumToHeaq(self, num):
        """
        添加元素到堆中——————》大顶堆中存储较大的一半的数据，小顶堆中存储较小的一半的数据
        Python 中 heapq 模块是小顶堆。
        实现 大顶堆 方法： 小顶堆的插入和弹出操作均将元素 取反 即可
        :param num:
        :return:
        """
        # 条件含义理解：始终要求小根堆的长度-大根堆的长度<=1，如果现在两个长度不等了，说明小根堆长度-大根堆长度=1，
        # 说明目前是奇数个，再加一个就是偶数个了，所以要放到大根堆里。怎么放呢？
        # 先把数放到小根堆，然后弹出小根堆的堆顶，放到大根堆。
        if len(self.minHeaq) != len(self.maxHeaq):
            heappush(self.maxHeaq, -heappushpop(self.minHeaq, num))
        else:
            heappush(self.minHeaq, -heappushpop(self.maxHeaq, -num))

    def findMedianInDataStreamPriorQueue(self):
        """
        方法二：使用优先队列查找中位数
        :return:
        复杂度分析：堆插入和删除需要O（logN）时间，即总体时间复杂度O（LogN），空间复杂度O（N）
        """
        # 如果两个堆的长度不相同，说明是奇数;反之是小顶堆的堆顶元素减去大顶堆的堆顶元素，因为大顶堆是经过小顶堆取负号变成的，元素全部为负数，因此是--
        return self.minHeaq[0] if len(self.minHeaq) != len(self.maxHeaq) else (self.minHeaq[0] - self.maxHeaq[0]) / 2


if __name__ == '__main__':
    s = Solution()
    print("-----------------第一种思路：二分查找-----------------------")
    s.addElement(num=1)
    s.addElement(num=2)
    s.addElement(num=7)
    s.addElement(num=9)
    s.addElement(num=3)
    s.addElement(num=4)
    s.addElement(num=1)
    print(s.store)
    print(s.findMedianInDataStreamBinarySearch())
    print("-----------------第二种思路：优先队列-----------------------")
    s.addNumToHeaq(2)
    s.addNumToHeaq(3)
    s.addNumToHeaq(8)
    s.addNumToHeaq(9)
    s.addNumToHeaq(1)
    s.addNumToHeaq(2)
    s.addNumToHeaq(3)
    s.addNumToHeaq(8)
    print("minHeaq:{}".format(s.minHeaq))
    print("maxHeaq:{}".format(s.maxHeaq))
    print(s.findMedianInDataStreamPriorQueue())
