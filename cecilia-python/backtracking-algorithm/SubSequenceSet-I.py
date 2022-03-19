#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   SubSequenceSet-I.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/30 22:17   cecilia      1.0        不包含重复元素集合的所有子集
问题描述：
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路分析：这种典型的问题存在三种解决方法——
1.递归。假设输出的最开始的子集为空集，后面每一个自己都向前进行添加新的整数，并生成新的子集。
比如最开始[[]]——> [[], [1]]——>[[], [1], [2]]——> [[],[1], [1,2]].....

2. 回溯法。
"""
from typing import List


def getSubSequenceSet(nums: List[int])->int:
    """
    第一种：简单递归，从空集入手
    [[]]——> [[], [1]]——>[[], [1], [2]]——> [[],[1], [1,2]]
    :param nums:
    :return:
    算法分析：时间复杂度O（N*2^N）, 空间复杂度O(N*2^N)
    """
    all_subsets = [[]]
    for i in range(len(nums)):
        all_subsets += [curr + [nums[i]] for curr in all_subsets]

    return all_subsets

def getSubSequenceSetForBacktrack(nums: List[int])->int:
    """
    第二种：回溯法。
    result = []
    def backtrack(路径, 选择列表):
        if 满足结束条件:
            result.add(路径)
            return
        for 选择 in 选择列表:
            做选择
            backtrack(路径, 选择列表)
            撤销选择
    :param nums:
    :return:
    算法分析：时间复杂度O（N*2^N）, 空间复杂度O(N*2^N)
    """
    if not nums:
        return 0

    result = []

    n = len(nums)

    def backtrack(index, tmp_list):
        """
        回溯过程
        :param index:
        :param tmp_list:
        :return:
        """
        result.append(tmp_list)

        # 如果选择在临时列表中
        for i in range(index, n):
            backtrack(i + 1, tmp_list + [nums[i]])

    backtrack(0, [])
    return result

def getSubSequenceSetForDictSort(nums):
    """
    第三种方法：字典排序（二进制排序） 子集(了解下即可)
    将每个子集映射到长度为 n 的位掩码中，其中第 i 位掩码 nums[i] 为 1，表示第 i 个元素在子集中；
    如果第 i 位掩码 nums[i] 为 0，表示第 i 个元素不在子集中。
    :param nums:
    :return:
    算法分析：时间复杂度O（N*2^N）, 空间复杂度O(N*2^N)
    """
    if not nums:
        return 0

    n = len(nums)

    result = []

    for i in range(2**n, 2**(n+1)):
        #  Return the binary representation of an integer and generate bitmask, from 0..00 to 1..11.
        bitmask = bin(i)[3:]

        # 当对应位为1时，挑选出来
        result.append([nums[j] for j in range(n) if bitmask[j] == '1'])

    return result






if __name__ == '__main__':
    nums = [1, 2, 3]
    # print(getSubSequenceSet(nums=nums))
    print(getSubSequenceSetForBacktrack(nums=nums))
    # print(getSubSequenceSetForDictSort(nums=nums))

