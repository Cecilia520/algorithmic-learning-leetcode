#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MaximumSubarray.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/7 14:31   cecilia      1.0        连续子数组最大的和
问题描述：
    给定一个整数数组nums，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大数组和

示例：
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶：
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""


def maximumSubarray(nums) -> int:
    """
    求取最大子数组和
    解决方案：贪心法
    算法思路：
    1.遍历数组，并记录当前每个元素的最大和；
    2.求数组的最大值
    :param nums: 整数数组
    :return:
    算法分析：时间复杂度O(N),空间复杂度O(1)
    """
    # 遍历数组，并记录每个元素的最大元素和
    current_sum = nums[0]
    maxsum = nums[0]
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum+nums[i])
        maxsum = max(current_sum, maxsum)
    return maxsum



def maximumSubarray2(nums) -> int:
    """
    求取最大子数组和
    算法思路：（参考题友的另一种解法）
        1.如果 sum > 0，则说明 sum 对结果有增益效果，则 sum 保留并加上当前遍历数字
        2.如果 sum <= 0，则说明 sum 对结果无增益效果，需要舍弃，则 sum 直接更新为当前遍历数字
        3.每次比较 sum 和 ans的大小，将最大值置为ans，遍历结束返回结果
    :param nums: 整数数组
    :return:
    算法分析：时间复杂度O(N),空间复杂度O(1)
    """
    maxsum = nums[0]
    current_sum = 0
    for num in nums:
        if current_sum > 0:
            print("num:{}".format(num))
            current_sum += num
        else:
            current_sum = num
        print("current_sum:{}".format(current_sum))
        maxsum = max(current_sum, maxsum)
    return maxsum


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maximumSubarray(nums))
