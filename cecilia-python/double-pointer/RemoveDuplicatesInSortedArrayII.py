#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   RemoveDuplicatesInSortedArrayII.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/24 18:07   cecilia      1.0       删除数组中的重复项(80题)

问题描述：
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:
给定 nums = [1,1,1,2,2,3],
函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
不需要考虑数组中超出新长度后面的元素。

示例 2:
给定 nums = [0,0,1,1,1,1,2,3,3],
函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。

算法思路：双指针
首先初始化两个指针i和j，还需要增加一个计数器cnt，用于判断元素相同的个数是否超过2个；
i从1开始索引数组，若当前元素和前一个元素相同，即nums[] == nums[i-1],那么cnt++；
    如果cnt>2，那么说明遇到了多余的重复项，此时我们只需要向前移动慢指针i，快指针不移动；
    如果cnt<=2,那么说明可以继续查找，将慢指针i移动到快指针j的位置，同时分别增加i和j；
如果当前元素和前一个元素不相同，即nums[i]!=nums[i-1],那么说明遇到了新的元素，此时更新cnt=1，并且将该元素移动到j位置，并同时增加i和j；
当数组遍历完成，返回j
"""


def removeDuplicatesInSortedArrayII(nums) -> int:
    """
    删除数组中的重复项(https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/)
    :param nums:
    :return:
    时间复杂度:O(N)
    空间复杂度：O(1)
    """
    j, cnt = 1, 1
    for i in range(1, len(nums)):
        # 如果当前的元素和前一个元素相同
        if nums[i] == nums[i - 1]:
            cnt += 1
            # 判断重复的次数是否超过2
        else:
            cnt = 1
        # 判断重复次数是否超过2
        if cnt <= 2:
            nums[j] = nums[i]  # 将当前索引位置i下的元素修改为索引位置j下的元素值
            j += 1  # 继续下一个元素

    return j


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(removeDuplicatesInSortedArrayII(nums))
