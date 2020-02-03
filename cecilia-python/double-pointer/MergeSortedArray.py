#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MergeSortedArray.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/16 16:07   cecilia      1.0       归并两个有序的数组
题目描述：给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
说明:
初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例：
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

参考链接：https://leetcode-cn.com/problems/merge-sorted-array/solution/he-bing-liang-ge-you-xu-shu-zu-by-leetcode/
"""
from typing import List


def mergesortedarray(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    """
    归并两个有序数组
    :param nums1:数组1
    :param m:
    :param nums2:数组2
    :param n:
    :return:
    思路一：直接法，先合并，然后排序
    算法分析：时间复杂度O((m+n)lg(m+n)),空间复杂度O(1)
    """
    nums1[:] = nums1[:m] + nums2
    return sorted(nums1)

def mergesortedarray1(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    """
    归并两个有序数组
    :param nums1:数组1
    :param m:
    :param nums2:数组2
    :param n:
    :return:
    思路一：双指针，从前开始
    算法分析：时间复杂度O(m+n),由于另外开辟了一个长度为m的数组对数据进行存储，所以空间复杂度O(m)
    """
    # copy data from nums1
    nums1_copy = nums1[:m]
    nums1[:] = [] # track the data
    print(nums1)

    # define double pointer
    i, j = 0, 0
    while i < m and j < n:
        if nums1_copy[i] < nums2[j]:
            nums1.append(nums1_copy[i])
            i = i + 1

        else:
            nums1.append(nums2[j])
            j = j + 1
    # if there are still elements to add
    if i < m:
        nums1[i + j:] = nums1_copy[i:]
    if j < n:
        nums1[i + j:] = nums2[j:]
    return nums1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(mergesortedarray1(nums1, m, nums2, n))
