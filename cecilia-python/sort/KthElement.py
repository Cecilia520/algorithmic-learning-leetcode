#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   KthElement.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/23 11:06   cecilia      1.0       找到第K个最大的元素
问题描述：Kth Largest Element in an Array (Medium)
例1
Input: [3,2,1,5,6,4] and k = 2
Output: 5
例2
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
"""
import heapq
from typing import List


def findKthLargest1(nums: List[int], k: int) -> int:
    """
    数组中第K个最大的元素
    :param nums:
    :param k:
    :return:
    解题思路一：直接排序，然后返回倒数第 K个元素
    算法分析：时间复杂度为 O(NlogN)，空间复杂度为 O(1)
    """
    return sorted(nums)[-k]

def findKthLargest2(nums: List[int], k: int) -> int:
    """
    数组中第K个最大的元素
    :param nums:
    :param k:
    :return:
    解题思路二：堆排序。
    创建一个大顶堆，将所有数组中的元素加入堆中，并保持堆的大小小于等于 k。这样，堆中就保留了前 k 个最大的元素。
    这样，堆顶的元素就是正确答案。像大小为 k 的堆中添加元素的时间复杂度为 O(logk)，我们将重复该操作 N 次，故总时间复杂度为 O(Nlogk)。
    在 Python 的 heapq 库中有一个 nlargest 方法，具有同样的时间复杂度，能将代码简化到只有一行。
    算法分析：时间复杂度为 O(NlogK)，空间复杂度为 O(k)，用于存储堆
    """
    return heapq.nlargest(k, nums)[-1]




if __name__ == '__main__':
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(findKthLargest2(nums, k))


