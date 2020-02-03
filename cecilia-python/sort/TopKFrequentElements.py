#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   TopKFrequentElements.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/16 16:07   cecilia      1.0       TopK出现频率最多的元素

题目描述：给定一个非空数组，返回频率最高的元素。
例如；
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

说明：
你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
"""
import collections
import heapq

def findTopKFrequent1(nums, k):
    """
    寻找出现频率最多的元素
    解决思路：首先遍历数组统计每个元素 出现的频数，并将其存储在HaspMap或者Dict中，
    然后对其进行维护，维护的方式有多种——
    第一种：最小堆：遍历Map或者Dict，利用最小堆来对高频前K个元素进行存储，每次都将新的元素与堆顶元素（最小的）进行比较，如果新的元素出现的频率比堆顶元素大，那么弹出堆顶元素，将新的元素添加到堆中；
    第二种：桶排序：遍历Map或者Dict，将频率作为数组的下标，对于出现频率不同的数字集合，存入对应的数组下标。
    解决方案一：直接法。遍历数据统计每个元素的频率，然后排序
    算法分析：时间复杂度O(nlogn),空间复杂度O(K)
    @:param nums 数组
    @:param k 前k个
    :return:
    """
    # 遍历数组，统计每个元素出现的频率
    counter = collections.Counter(nums)
    print(counter.keys())
    # 针对valves进行排序
    res = sorted(counter.items(), key=lambda x: x[1], reverse=True) # x[1]表示对values进行排序，x[0]表示对keys进行排序
    print(res)
    answers = []
    # 遍历dict，对排序后的dict进行获取前k个元素
    for (key, valve) in res:
        if k > 0:
            answers.append(key)
            k -= 1
        else:
            break
    return answers

def findTopKFrequent2(nums, k):
    """
    解决方案二：使用最小堆进行排序，切忌使用大顶堆!!!
    :param nums:
    :param k:
    :return:
    算法分析：Counter方法的时间复杂度是O(N), 创建堆和输出的时间复杂度O(nlogK)，总体的时间复杂度是O(NlogK);空间复杂度O(N)
    """
    counter = collections.Counter(nums)
    answers = heapq.nlargest(k, counter.keys(), key=counter.get) # 如果当K无限大的情况，可以使用nsmallest()改成删除频率最低的若干个元素。
    return answers

def findTopKFrequent3(nums, k):
    """
    解决方案三：桶排序。
    将数组统计每个元素的频率，并存储在字典中；
    根据最大次数创建一个桶，然后按照桶的索引进行排序，最后输出
    :param nums:
    :param k:
    :return:
    算法分析：时间复杂度O(N),空间复杂度O(N)
    """
    counter = collections.Counter(nums)
    # 根据最大次数创建一个桶
    max_count = max(counter.values())
    bucketList= [[] for i in range(max_count+1)]

    for (key, value) in counter.items():
        bucketList[value].append(key)
    print(bucketList)
    answers = []
    for i in range(max_count, 0, -1): # 按照桶的索引排序
        if bucketList[i]:
            answers.extend(bucketList[i]) # 将可迭代对象迭代后追加到其中
        # 如果answers超过了k，则截取
        if len(answers) > k:
            return answers[:k]
    return answers



if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1, 2, 2, 3, 3, 2, 2, 2, 2, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 8, 9]
    k = 2
    print(findTopKFrequent3(nums, k))

