#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   NineBinaryAdder.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/19 17:56   cecilia      1.0        九进制加法运算
问题描述：
在太空深处，生活着一群外星人，他们左手有4个手指，右手有5个手指，所以自然地，他们习惯采用9进制记数。不过，
这外星人还没有点亮“计算机科技”，所以向地球的你发出了求助，希望你帮他们设计一款
可以用来完成9进制的加法程序。

示例1：
输入：
"1.28","1.71"
输出：
"3.10"

示例2：
输入：
"25", "15"
输出：
"41"

注意：数字可能是小数，数字的整数部分不超过100位，小数部分不超过60位
"""
#
# 接收两个表示9进制数的字符串，返回表示它们相加后的9进制数的字符串
# @param num1 string字符串 第一个加数
# @param num2 string字符串 第二个加数
# @return string字符串
#
import sys


class Solution:
    def add_int(self, a: str, b: str):
        """
        整数加法
        """
        aL = len(a)
        bL = len(b)
        maxL = max(aL, bL)
        # 是否进位
        carry = 0
        res = ""
        for i in range(maxL):
            cur_a = 0
            cur_b = 0
            if i < aL:
                cur_a = int(a[aL - i - 1])
            if i < bL:
                cur_b = int(b[bL - i - 1])
            cur_res_tmp = cur_a + cur_b + carry
            # 判断进位
            if cur_res_tmp >= 9:
                carry = 1
            else:
                carry = 0
            cur_res = cur_res_tmp % 9
            res = str(cur_res) + res
        if carry == 1:
            res = "1" + res
        return res

    def add_decimal(self, dec_a: str, dec_b: str):
        """
        计算小数部分
        :param dec_a:
        :param dec_b:
        :return:
        """
        dec_a_copy = dec_a
        dec_b_copy = dec_b
        if len(dec_a) > len(dec_b):
            dec_b_copy = dec_b + "0" * (len(dec_a) - len(dec_b))
        else:
            dec_a_copy = dec_a + "0" * (len(dec_b) - len(dec_a))
        dec_res = self.add_int(dec_a_copy, dec_b_copy)  # 按照整数那样进行加法
        carry = False  # 进位标识
        if len(dec_res) > len(dec_a_copy):
            carry = True
            dec_res > dec_res[1:]
        return carry, dec_res

    def add(self, num1, num2):
        #  先做加法，再转化为9进制数
        # 按照.进行分割
        a_step = num1.split(".")
        b_step = num2.split(".")
        if len(a_step) == 1 and len(b_step) == 1:
            return self.add_int(num1, num2)
        left_res = self.add_int(a_step[0], b_step[0])
        right_res = ""
        if len(a_step) == 2 and len(b_step) == 2:
            carry, right_res = self.add_decimal(a_step[1], b_step[1])
            if carry:
                left_res = self.add_int(left_res, "1")
        else:
            if len(a_step) == 2:
                right_res = a_step[1]
            else:
                right_res = b_step[1]
        return left_res + "." + right_res


if __name__ == "__main__":
    # num1, num2 = map(str, sys.stdin.readline().strip().split(','))
    num1 = "25"
    num2 = "41"
    s = Solution()
    print(s.add(num1, num2))