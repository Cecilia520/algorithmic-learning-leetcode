#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   NormalizationNumber.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/23 20:23   cecilia      1.0        规范化数字
货币数值的规范化是金融公司的一个问题，现在你需要写一个程序来解决这一问题：

1.货币数值的整数部分要求每3位加一个英文逗号','（不含引号）。例如12345678应该规范化为12,345,678

2.货币数值最多只有两位小数，如果有多余的小数位数应当舍去。注意，不是四舍五入。

3.负数代表欠款，在规范化后应当在数值两端加上括号 '(' 和 ')' ，然后省略掉负号。

4.应当在数值前面，前括号后面（如果有括号的话）加上金钱符号'$'（不含引号）

现在给你一个数字，请你规范化这一数字

输入
输入包含多种数据，每组数据一行一个数字，可能为小数，整数，负整数，负小数或者零。

数据保证数字没有前导0，保证不会出现欠0元的情况

输出
输出规范化后的内容


样例输入
203323
0.0
0.000000
0.009212121
343444323.32432
-12344.1
-12345678.9

样例输出
$203,323.00
$0.00
$0.00
$0.00
$343,444,323.32
($12,344.10)
($12,345,678.90)

提示
范围
每个字符串长度不会超过100
"""


class Solution:
    def normalizationNumber(self, input_str):
        """
        暴力法
        :param num:
        :return:
        """
        left = ""
        right = ""
        for input_str in input_list:
            left_right = list(map(str, input_str.split(".")))
            if len(left_right) <= 1:
                left = left_right[0]
            else:
                left = left_right[0]
                right = left_right[1]
            if len(right) == 0:
                right += '00'
            elif len(right) == 1:
                right += '0'
            elif len(right) > 2:
                right = right[0:2]

            if int(left) >= 0:
                print("$" + self.getLeftNum(left) + "." + right)
            else:
                print("($" + self.getLeftNum(left) + "." + right + ")")

    def getLeftNum(self, left):
        """
        处理左边的数据
        :param left:
        :return:
        """
        i = len(left) - 1
        j = len(left) - 3
        res = ","
        while i - j == 2:
            res = "," + left[j:i + 1] + res
            i = i - 3
            j = j - 3
            if j < 0:
                j = 0
                res = left[j:i + 1] + res
        return res.strip(",")


if __name__ == '__main__':
    input_list = []
    for line in iter(input, ''):
        input_list.append(line.replace(',', ''))
    print(input_list)
    s = Solution()
    res = s.normalizationNumber(input_list)
    print(res)
