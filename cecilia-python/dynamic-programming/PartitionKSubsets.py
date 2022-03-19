#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PartitionKSubsets.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/30 22:18   cecilia      1.0        划分为k个相等的子集
问题描述：
给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。

示例 1：
输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
 
注意:
1 <= k <= len(nums) <= 16
0 < nums[i] < 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections


def getPartitionKSubsets(nums, k):
    """
    判断是否可以切割成k个和相等的子集
    暴力法：首先求解所有的子集，然后计算所有的子集的和，计算和相等的个数是否存在为k，如果存在，那么True,否则False
    :param nums:
    :param k:
    :return:
    """
    # # 回溯法或者递归法找出所有的子集
    # def backtrack(index, n, tmp_list):
    #     # if tmp_list not in all_subset:
    #     all_subset.append(tmp_list)
    #     for i in range(index, n):
    #         backtrack(i+1, n, tmp_list+[nums[i]])

    if not nums or k < 0:
        return False

    nums = sorted(nums)

    n = len(nums)

    if k > n:
        return False

    all_subset = [[]]

    for num in nums:
        all_subset += [curr + [num] for curr in all_subset]

    # backtrack(0, n, [])

    print(all_subset)

    # 计算所有子集的和
    subsum = []
    for subset in all_subset:
        if len(subset) >= 1:
            tmpsum = 0
            for i in range(len(subset)):
                tmpsum += subset[i]
            subsum.append(tmpsum)

    print(subsum)

    dictSum = collections.Counter(subsum)
    print(dictSum)

    if k in dictSum.values():
        return True
    else:
        return False


if __name__ == '__main__':
    # print(getPartitionKSubsets(nums=[4, 3, 2, 3, 5, 2, 1], k=4))
    print(getPartitionKSubsets(nums=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], k=5))
