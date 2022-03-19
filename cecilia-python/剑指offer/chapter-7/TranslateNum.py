#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   TranslateNum.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/8/20 17:25   cecilia      1.0        将数字翻译成字符串（动态规划）
问题描述：
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

 示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
'''
思路分析：
    这道题主要考查的是如何地推出状态转移方程，可以将数字堪称x1x2x3x4x5...，整体翻译的方案数是等于单独翻译xi时的方案总数；因此，
    方案数的递推公式:
        f（i） = f(i-2) + f(i-1),当xi-1xi可被翻译时；反之f(i)=f(i-1)
        
优化思路：
    主要是从空间上考虑优化，可以采用数据求余的思路进行优化空间，
'''


class Solution:
    def translateNum(self, num: int) -> int:
        """
        将数字翻译成字符串
        :param num:
        :return:
        复杂度分析：时间复杂度O（N），空间复杂度O（N），N为字符串的长度，决定了循环的次数
        """
        str_num = str(num)
        a, b = 1, 1
        for i in range(len(str_num) - 2, -1, -1):
            a, b = (a + b if "10" <= str_num[i: i + 2] <= "25" else a), a
        return a

    def translateNumPlus(self, num: int) -> int:
        """
        将数字翻译成字符串
        优化：利用求余运算 num \% 10num%10 和求整运算 num // 10num//10 ，可获取数字 numnum 的各位数字（获取顺序为个位、十位、百位…）。
        :param num:
        :return:
        复杂度分析：时间复杂度O（N），空间复杂度O（1），N为字符串的长度，决定了循环的次数
        """
        a = 1
        b = 1
        y = num % 10
        while num != 0:
            num //= 10
            x = num % 10
            tmp = 10 * x + y
            c = a + b if 10 <= tmp <= 25 else a
            b, a = a, c
            y = x
        return a


if __name__ == '__main__':
    s = Solution()
    print(s.translateNumPlus(num=12258))
