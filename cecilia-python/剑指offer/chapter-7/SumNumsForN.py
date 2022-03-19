#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   SumNumsForN.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/8/21 17:40   cecilia      1.0       不用乘除做1+2+3+4+...+n的和（位运算）
问题描述：
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

示例 1：

输入: n = 3
输出: 6
示例 2：

输入: n = 9
输出: 45

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qiu-12n-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
'''
这道题要求不能使用乘除、if/else 、switch等条件语句，那么可以考虑短路逻辑运算符—— “与 && ”，“或 || ”，“非 !” ，有重要的短路效应：

if(A && B)  // 若 A 为 false ，则 B 的判断不会执行（即短路），直接判定 A && B 为 false

if(A || B) // 若 A 为 true ，则 B 的判断不会执行（即短路），直接判定 A || B 为 true

'''
class Solution:
    def SumNumsForN(self, n)->int:
        """
        位运算计算从1+2+3+4+....+n的和
        :param n:
        :return:
        复杂度分析：时间复杂度O（N），不要开启n+（n-1）+（n-2）+...1个递归函数，空间复杂度O（1）
        """
        self.res = 0
        # 利用与运算的短路效应递归计算和
        n > 1 and self.SumNumsForN(n-1)
        self.res += n
        return self.res

if __name__ == '__main__':
    s = Solution()
    print(s.SumNumsForN(n=10))
