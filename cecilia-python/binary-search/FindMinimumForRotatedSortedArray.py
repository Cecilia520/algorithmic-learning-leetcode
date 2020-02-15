#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   FindMinimumForRotatedSortedArray.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/15 13:33   cecilia      1.0       旋转数组的最小数字
问题描述：
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
请找出其中最小的元素。

注意：可以假设数组中不存在重复元素。

示例 1:
输入: [3,4,5,1,2]
输出: 1

示例 2:
输入: [4,5,6,7,0,1,2]
输出: 0

问题分析：
由于给定的数组是有序的，我们就可以使用二分搜索。然而，数组被旋转了，所以简单的使用二分搜索并不可行。
在这个问题中，我们使用一种改进的二分搜索，判断条件与标准的二分搜索有些不同。
数组旋转过了。这是因为原先的数组为 [2, 3, 4, 5, 6, 7]，通过旋转较小的元素 [2, 3] 移到了后面，也就是 [4, 5, 6, 7, 2, 3]。因此旋转数组中第一个元素 [4] 变得比最后一个元素大。
这意味着在数组中你会发现一个变化的点，这个点会帮助我们解决这个问题，我们称其为变化点。

在这个改进版本的二分搜索算法中，我们需要找到这个点。下面是关于变化点的特点：
1.所有变化点左侧元素 > 数组第一个元素
2.所有变化点右侧元素 < 数组第一个元素

算法分析：

1.找到数组的中间元素 mid。

2.如果中间元素 > 数组第一个元素，我们需要在 mid 右边搜索变化点。

3.如果中间元素 < 数组第一个元素，我们需要在 mid 做边搜索变化点。


"""


def findMinimumForRotatedSortedArray(rotatedarr) -> int:
    """
    在旋转有序数组中寻找最小的元素
    常规二分法思路
    :param rotatedarr:
    :return:
    """
    if len(rotatedarr) == 1:
        return rotatedarr[0]

    l, h = 0, len(rotatedarr) - 1

    while l < h:
        mid = int(l + (h - l) / 2)
        if rotatedarr[mid] <= rotatedarr[h]:
            h = mid
        else:
            l = mid + 1
    return rotatedarr[l]


def findMinimumForRotatedSortedArray1(rotatedarr) -> int:
    """
    在旋转有序数组中寻找最小的元素
    改进思路：寻找变化点
    参考：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/solution/xun-zhao-xuan-zhuan-pai-lie-shu-zu-zhong-de-zui-xi/
    :param rotatedarr:
    :return:
    """
    if len(rotatedarr) == 1:
        return rotatedarr[0]

    # left pointer
    left = 0
    # right pointer
    right = len(rotatedarr) - 1

    # 如果最后一个元素比第一个元素要大，说明当前数组没有被旋转
    # e.g. 1 < 2 < 3 < 4 < 5 < 7.
    # 因此最小的元素就是第一个元素 A[0]
    if rotatedarr[right] > rotatedarr[0]:
        return rotatedarr[0]

    # 如果是旋转了，那么采用二分法搜索
    while right >= left:
        # 计算中间元素
        mid = int(left + (right - left) / 2)
        # 如果中间元素比下一个元素要大，那么mid+1就是最小的元素
        if rotatedarr[mid] > rotatedarr[mid + 1]:
            return rotatedarr[mid + 1]
        # 如果中间元素比前一个元素要小，那么当前mid就是最小的元素
        if rotatedarr[mid - 1] > rotatedarr[mid]:
            return rotatedarr[mid]

        # 如果中间元素比第一个元素要大，说明需要往右区间进行搜索
        if rotatedarr[mid] > rotatedarr[0]:
            left = mid + 1
            # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left
        else:
            right = mid - 1


if __name__ == '__main__':
    # rotatedarr = [3,4,5,1,2]
    rotatedarr = [4, 5, 6, 7, 0, 1, 2]
    print(findMinimumForRotatedSortedArray1(rotatedarr))
