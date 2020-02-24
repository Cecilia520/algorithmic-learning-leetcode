#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   RemoveDuplicatesInSortedArray.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/24 17:19   cecilia      1.0       删除数组中的重复项（26题）
问题描述：
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用O(1)额外空间的条件下完成。


示例：
给定数组nums = [1,1,2],
输入格式为[1,1,2]

输出：2。函数应该返回新的长度2,并且原数组nums的前两个元素被修改为1, 2。
你不需要考虑数组中超出新长度后面的元素。

算法思路：双指针
数组完成排序后，我们可以放置两个指针 i 和 j，其中 i 是慢指针，而 j 是快指针。
若nums[i]=nums[j]，增加 j 以跳过重复项；
若nums[j]≠nums[i] 时，i++，即找到一个不一样的数字，此时需要将当i索引下的元素修改为当前遍历j的元素值——nums[i] = nums[j];
最后统计的i即使删除后的数组的长度。
"""


def removeDuplicatesInSortedArray(nums) -> int:
    """
    删除数组中的重复项（https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/）
    :param nums:
    :return:
    时间复杂度：O(N)
    空间复杂度：O(1)
    """
    if len(nums) == 0:
        return 0
    i = 0  # 慢指针
    for j in range(1, len(nums)):  # 快指针
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(removeDuplicatesInSortedArray(nums))
