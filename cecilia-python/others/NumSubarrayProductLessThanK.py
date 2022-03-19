#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   NumSubarrayProductLessThanK.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/12 14:27   cecilia      1.0        连续子序列乘积小于K的个数
问题描述：
给定一个正整数数组 nums。

找出该数组内乘积小于 k 的连续的子数组的个数。

示例 1:

输入: nums = [10,5,2,6], k = 100
输出: 8
解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于100的子数组。

链接：https://leetcode-cn.com/problems/subarray-product-less-than-k
"""


def numSubarrayProductLessThanK(nums, k):
    """
    统计连续子序列乘积小于k的个数
    思路分析：
    1.二分查找法
       参考https://leetcode-cn.com/problems/subarray-product-less-than-k/solution/cheng-ji-xiao-yu-kde-zi-shu-zu-by-leetcode/并不是特别明白！
    2.最优化的思路：
      最关键的是确定（left,right）的乘积小于k的最小left，比如[2,6]满足小于20，[3,6]也满足小于20，但是[2,6]中left最小的是2
    :param nums:
    :return:
    算法分析：时间复杂度O(N)，空间复杂度O(1)
    """
    if k <= 1:
        return 0

    mutilVal = 1

    l = 0
    result = 0  # 存储每一次的乘积结果

    for r, cur in enumerate(nums):
        mutilVal = mutilVal * cur

        while mutilVal >= k:
            mutilVal = mutilVal / nums[l]  # 当乘积超过k，那么需要除以左边的数据，直到乘积小于k
            l += 1

        # 乘积小于k，那么计算个数：(r -l + 1)代表的是当前的满足乘积小于k的区间长度，也就是个数
        result = result + (r - l + 1)

    return result


if __name__ == '__main__':
    print(numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
