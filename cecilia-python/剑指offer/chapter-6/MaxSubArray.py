#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MaxSubArray.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/27 17:43   cecilia      1.0       获连续数组中最大值
问题描述：
输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
 

提示：

1 <= arr.length <= 10^5
-100 <= arr[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
'''
思路分析：
   实质上考察动态规划此题中可以使用nums作为dp数组，
   当nums【i】> 0: nums[i] = nums[i] + nums[i - 1]
'''

class Solution:
    def getMaxSubArray(self, nums):
        """
        连续数组中的最大值
        :param nums:
        :return:
        复杂度分析：时间复杂度O（N），空间复杂度O（1）
        """
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.getMaxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
