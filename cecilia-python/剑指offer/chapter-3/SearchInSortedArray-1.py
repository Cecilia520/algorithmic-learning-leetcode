#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   SearchInSortedArray-1.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/14 16:50   cecilia      1.0       查找排序数组中的元素(二分查找)
问题描述：
统计一个数字在排序数组中出现的次数。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
"""
'''
对于排序数组中的查找元素，首先想到的解决方案就是二分查找法，具体需要注意边界条件、区间以及返回值
对于该题中，需要二分查找两次，分别找到和target相等的元素的left和right边界位置
算法思路：
1.设定left=0，right=len（nums）-1;
2.计算mid = (left+right)//2
3.如果nums[mid] > target,说明target在【left，mid-1】区间中，left = mid-1；
4.如果nums[mid] < target,说明target在【mid+1，right】区间中，right=mid+1；
5.如果nums[mid] = target,说明右边界在【mid+1， right】，左边界在【left，mid-1】，此时：
left = mid + 1, right = mid - 1；
'''
class Solution:
    def SearchInSortedArray(self, nums, target):
        """
        查找数组中指定元素的出现的次数
        方法：直接遍历法
        :param nums:
        :return:
        """
        if not nums:
            return 0
        cnt = 0
        for i in nums:
            if i == target:
                cnt += 1
        return cnt

    def SearchInSortedArrayBinary(self, nums, target):
        """
        二分法查找数据，并统计次数
        :param nums:
        :param target:
        :return:
        """
        def binarySearch(target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        return binarySearch(target) - binarySearch(target - 1)

if __name__ == '__main__':
    s = Solution()
    print(s.SearchInSortedArrayBinary())
