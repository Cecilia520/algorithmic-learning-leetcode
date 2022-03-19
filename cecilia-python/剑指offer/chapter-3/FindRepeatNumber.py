#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   FindRepeatNumber.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/14 16:37   cecilia      1.0       查找数组中重复出现的数据
问题描述：
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，
也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
'''
最简单的思路就是遍历数组，然后使用哈希表统计每个元素的出现次数，这样的时间复杂度和空间复杂度都是O(N)，
由于没有重复出现的数据比较少的，这种策略还是阔以的
'''
class Solution:
    def FindRepeatNumber(self, nums):
        """
        查找数组中重复出现的数据
        哈希表存储没有重复出现过的数据
        :param nums:
        :return:
        复杂度分析：时间复杂度O（N），空间复杂度O（N）
        """
        # 使用哈希表存储没有重复出现过的数据
        hash_dict = {}
        for num in nums:
            if num not in hash_dict:
                hash_dict[num] = 0
            else:
                return num


if __name__ == '__main__':
    s = Solution()
    nums = [2, 3, 1, 0, 2, 5, 3]
    print(s.FindRepeatNumber(nums=nums))

