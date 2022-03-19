#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   CountContinuousSequence-2.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/9 10:25   cecilia      1.0        数组中数字出现的次数 II(考察位运算)
问题描述：
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

示例 1：

输入：nums = [3,4,3,3]
输出：4
示例 2：

输入：nums = [9,1,7,9,7,9,7]
输出：1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
'''
该题和1有所相似，思路相差不多，但是现在数组中数据除了出现一次，还有出现三次的元素，
对于我们而言，可以将其所有的元素出现次数和元素存储在哈希表中，但是这样空间复杂度有所被利用了，
为了更好的实现空间复杂度为O（1），时间复杂度为O2（N）

思路分析：

'''


class Solution:
    def CountContinuousSequence2(self, nums) -> int:
        """
        找出数组中统计除了出现3次的数据
        方法：位运算
        :param nums:
        :return:
        时间复杂度O(N)，空间复杂度O（1）
        """
        res = 0
        for i in range(32):
            cnt = 0  # 记录当前bit有多少个1
            bit = 1 << i
            for num in nums:
                if num & bit != 0:
                    cnt += 1
            if cnt % 3 != 0:
                # 不等于1说明唯一出现的数字在bit上是1
                res |= bit
        return res - 2 ** 32 if res > 2 ** 31 - 1 else res

    def CountContinuousSequence2Plus(self, nums) -> int:
        """
        使用有穷自动机来解决实际问题，此种方法比较适合当前场景，但是不是用其他的，比如n个数据出现一次的情形
        :param nums:
        :return:
        """
        two, one = 0, 0  # 初始状态
        for num in nums:
            one = one ^ num & ~two
            two = two ^ num & ~one
        return one


if __name__ == '__main__':
    s = Solution()
    print(s.CountContinuousSequence2(nums=[3, 5, 3, 3, 4, 4, 4]))
    print(s.CountContinuousSequence2Plus(nums=[3, 5, 3, 3, 4, 4, 4]))

