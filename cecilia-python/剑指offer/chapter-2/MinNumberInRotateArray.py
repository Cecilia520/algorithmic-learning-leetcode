#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MinNumberInRotateArray.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/9 10:11   cecilia      1.0        旋转数组的最小数字
问题描述：
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1

示例 2：

输入：[2,2,2,0,1]
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
'''
思路分析：
旋转数组存在一个比较特殊的地方，就是旋转数组的最小元素的位置比左边元素大，比右边元素小，利用这个关键点可以对数组进行遍历
遍历方法存在两种：
第一，直接从头到尾遍历，直到出现转折点的位置,通常这种情况都会超时，不推荐；
第二，二分法查找法。
选定区间【i，j】表示当前搜索的区间，i从0开始，j从len(numbers)开始，其中m=i + int((j-i)/2)，是向下取整，旋转点i<=m<j,右区间是开放的
当numbers[m] > numbers[j]时，说明旋转点在【m+1，j】内，由于按照规律的话，中间索引对应的值一定小于最右边的值，即i = m+1
当numbers[m] < numbers[j]时，说明旋转点在【i，m】区间内，即j=m；
当numbers[m] = numbers[j]时，此时无法判断旋转点在哪，可能会出现[4,4,4,2,2,2,2]的情况，那么可以减少j，不断变化观察，即j--

'''
class Solution:
    def MinNumberInRotateArray(self, nums):
        """
        查找旋转数组中最小的元素
        :param nums:
        :return:
        时间复杂度分析：时间复杂度O(N)
        """
        if not nums:
            return 0
        for i in range(1, len(nums) - 1):
            if nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                return nums[i]

    def MinNumberInRotateArrayPlus(self, nums):
        """
        查找旋转数组中最小的元素
        :param nums:
        :return:
        时间复杂度分析：时间复杂度O(logN)
        """
        if not nums:
            return None
        i, j = 0, len(nums)-1
        while i < j:
            m = i + int((j - i) / 2)
            if nums[m] > nums[j]:
                i = m + 1
            elif nums[m] < nums[j]:
                j = m
            else:
                j -= 1
        return nums[i]


if __name__ == '__main__':
    s = Solution()
    nums = [4, 4, 4, 1, 2]
    print(s.MinNumberInRotateArray(nums=nums))
    print(s.MinNumberInRotateArrayPlus(nums=nums))
