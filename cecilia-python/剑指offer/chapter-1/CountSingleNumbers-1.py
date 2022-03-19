#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   CountSingleNumbers-1.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/9 10:27   cecilia      1.0        寻找数组中只出现一次的元素
问题描述：
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。
请写程序找出这两个只出现一次的数字。
要求时间复杂度是O(n)，空间复杂度是O(1)。
示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
'''
刚开始看到这道题的时候，最开始想到的是遍历统计，使用哈希表来存储每种数据的次数，但是这种方案不满足空间复杂度为O(1)；另外一种就是直接遍历，但是不满足时间复杂度为O(n)的要求，
那么只能使用异或来解决这道题，异或的关键点：
** 异或的性质
- 两个数字异或的结果a^b是将 a 和 b 的二进制每一位进行运算，得出的数字。 运算的逻辑是
- 如果同一位的数字相同则为 0，不同则为 1
** 异或的规律
- 任何数和本身异或则为 0
- 任何数和 0 异或是 本身
- 异或满足交换律。 即 a ^ b ^ c ，等价于 a ^ c ^ b


思路：对于出现两个出现次数为1的情况，可以考虑异或先进行分组，然后再将每一组的数据进行异或得到两个出现次数为1的数据
其中分组需要满足两个条件：
第一，两个独特的数据分成不同的组；
第二，相同的数据分在同相同组。
'''
class Solution:
    def CountSingleNumbers(self, nums):
        """
        通过异或分组解决问题,找出数组中出现次数为1的两个数据
        :param nums:
        :return:
        复杂度分析：O(N),空间复杂度O（1）
        """
        tmp1 = 0
        for i in nums:
            tmp1 ^= i
        flag = 1
        # 找到第一位不是0的分界点
        while tmp1 & flag == 0:
            flag = flag << 1

        res1 = 0
        res2 = 0
        for num in nums:
            # 判断该位是否为0，可以将其分组
            if flag & num == 0:
                res1 ^= num
            else:
                res2 ^= num
        return [res1, res2]

if __name__ == '__main__':
    s = Solution()
    print(s.CountSingleNumbers(nums=[1, 2, 10, 4, 1, 4, 3, 3]))
