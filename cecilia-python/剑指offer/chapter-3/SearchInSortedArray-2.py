#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   SearchInSortedArray-2.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/14 16:50   cecilia      1.0       在递增数组中查找缺失值
问题描述：
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

示例 1:

输入: [0,1,3]
输出: 2
示例 2:

输入: [0,1,2,3,4,5,6,7,9]
输出: 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
'''
方法一：直接遍历，找下标和下表对应的值是否相等——》时间复杂度O(N)
方法二：二分法——。时间复杂度O（N）

注意：数组长度为n-1！！！！
'''
class Solution:
    def SearchInSortedArray(self, nums):
        """
        直接遍历法查找缺失值
        :param nums:
        :return:
        """
        if not nums:
            return None
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

    def SearchInSortedArrayBinarySearch(self, nums):
        """
        二分法查找缺失值
        :param nums:
        :return:
        """
        if not nums:
            return None
        i, j = 0, len(nums)
        while i <= j:
            mid = i + int((j-i)/2)
            if mid == nums[mid]:
                i = mid + 1
            else:
                j = mid - 1
        return i

if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 3]
    print(s.SearchInSortedArray(nums=nums))
    print(s.SearchInSortedArrayBinarySearch(nums=nums))