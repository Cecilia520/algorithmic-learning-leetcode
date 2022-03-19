#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   SubSequenceSet-IIpy
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/30 22:16   cecilia      1.0       包含重复元素的集合的所有子集
问题描述：给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""
from typing import List


def getSubSequenceSet(nums: List[int]) -> int:
    """
    和子集-I的思路一致，就是中间需要一个去重的过程
    :param nums:
    :return:
    """
    if not nums:
        return 0

    n = len(nums)

    nums = sorted(nums)

    result = []

    def backtrack(index, n, tmp_list):
        # 如果临时的不在结果列表中，则添加,题目要求是解集中不能包含重复的子集
        if tmp_list not in result:
            result.append(tmp_list)

        for i in range(index, n):

            # 如果此处需要返回的是重复的元素不算一个子集，如果[1,2,2]，他的子集只能是[[], [1],[2], [1,2]],可以加入此行代码
            # if nums[i] == nums[i-1]:
            #     continue
            # 回溯上一个
            backtrack(i + 1, n, tmp_list + [nums[i]])

    backtrack(0, n, [])
    return result


if __name__ == '__main__':
    print(getSubSequenceSet(nums=[1, 2, 2]))
