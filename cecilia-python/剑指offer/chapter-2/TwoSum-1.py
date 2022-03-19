#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   TwoSum-1.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/9 10:08   cecilia      1.0         和为S的两个数字
问题描述：
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
示例 2：

输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

'''
根据一个数组nums，可以设定两个指针i和j，分别从数组的头和尾开始，每次计算两个指针指向的数据的和s，
当s > target时，需要j--
当s < target时，需要i++
否则是i和j对应的值
'''


class Solution:
    def TwoSum(self, nums: List[int], target: int)-> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s < target:
                i += 1
            elif s > target:
                j -= 1
            else:
                return [nums[i], nums[j]]
        return []

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums)
        while i < j:
            cur_sum = nums[i] + nums[j]
            if cur_sum > target:
                j -= 1
            elif cur_sum < target:
                i += 1
            else:
                return [nums[i], nums[j]]
        return []


if __name__ == '__main__':
    s = Solution()
    nums = [10, 26, 30, 31, 47, 60]
    print(s.TwoSum(nums, target=40))
