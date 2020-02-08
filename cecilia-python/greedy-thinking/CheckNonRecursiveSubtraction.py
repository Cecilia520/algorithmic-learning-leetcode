#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   CheckNonRecursiveSubtraction.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/8 14:47   cecilia      1.0         判断是否称为非递减数列
问题描述：
给定一个整数数组，判断在最多改变一个元素的情况下，该数组能否变成一个非递减数列
非递减数列定义：
    对于数组中所有的 i (1 <= i < n)，满足 array[i] <= array[i + 1]。

示例1：
输入: [4,2,3]
输出: True
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。

示例2：
输入: [4,2,1]
输出: False
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。

说明:  n 的范围为 [1, 10,000]。
"""
def checkNonRecursiveSubtraction(nums) -> bool:
    """
    思路：
        当nums[i] < nums[i-1]时，需要考虑的是应该修改数组的哪个数，使得本次数组是非递减数组，并且不影响后续的操作。
        优先考虑令nums[i-1]=nums[i],如果是反过来的话，即nums[i]=nums[i-1]，那么nums[i]的数就会变大，甚至比nums[i+1]还可能大，影响了后续操作。
        还有一个特别的情况，Nums[i] < nums[i-2],修改Nums[i-1]=nums[i]不能使数组成为非递减数组，此时可以修改成nums[i]=nums[i-1]
    :param nums:
    :return:
    """
    cnt = 0
    if cnt < 2:
        for i in range(1, len(nums)):
            # 如果前面的元素比当前的元素小，继续寻找
            if nums[i] >= nums[i - 1]:
                continue
            cnt += 1
            # 如果遍历到2个元素以及以上，并且前面第二个元素比当前的元素都大
            if i >= 2 and nums[i - 2] > nums[i]:
                nums[i] = nums[i - 1] # 可以采取将前面第一个元素的值修改为当前元素的值
                print("第一种情形：{}".format(nums))
            else:
                # 如果只有2个元素以下，或者前面的元素比当前的元素小
                nums[i - 1] = nums[i]
                print("第二种情形：{}".format(nums))

        return cnt <= 1


if __name__ == '__main__':
    nums = [4, 3, 2]
    print(checkNonRecursiveSubtraction(nums))
