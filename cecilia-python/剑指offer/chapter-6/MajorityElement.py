#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MajorityElement.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/27 14:49   cecilia      1.0       寻找数组中出现次数超过数组长度的一半
问题描述：
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
示例 1:

输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
 

限制：

1 <= 数组长度 <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
'''
解决思路一：哈希表法
   直接遍历，记录每个元素的出现次数，如果该元素出现次数超过数组长度的一半，那么直接return；
解决思路二：正负抵消法
   如果当前投票数vote=0，那么num=x；
   遍历数组，如果vote=0，那么num=x；
   否则如果num=x，那么vote+=1，否则减1
'''
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        寻找数组中出现次数超过数组长度的一半（哈希表法）
        :param nums:
        :return:
        复杂度分析：时间复杂度O（N）
        """
        hashdict = {}
        for i in range(len(nums)):
            if nums[i] not in hashdict:
                hashdict[nums[i]] = 1
            else:
                hashdict[nums[i]] += 1
            if hashdict[nums[i]] > len(nums) // 2:
                return nums[i]

    def majorityElementPlus(self, nums: List[int]) -> int:
        """
        正负抵消法（摩尔投票法）
        :param nums:
        :return:
        复杂度分析：时间复杂度O（N），空间复杂度O（1）
        """
        votes = 0
        for num in nums:
            if votes == 0:
                x = num
            votes += 1 if num == x else -1
        return x

if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement(nums=[1, 2, 3, 2, 2, 2, 5, 4, 2]))
    print(s.majorityElementPlus(nums=[1, 2, 3, 2, 2, 2, 5, 4, 2]))

