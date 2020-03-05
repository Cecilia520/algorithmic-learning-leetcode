#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ExcelSheetColumnTitle.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/3 19:01   cecilia      1.0         给定一个正整数，返回它在 Excel 表中相对应的列名称。
问题描述：给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
示例 1:

输入: 1
输出: "A"
示例 2:

输入: 28
输出: "AB"
示例 3:

输入: 701
输出: "ZY"
"""


def excelSheetColumnTitle(num):
    """
    将整数转化成Excel表中对应的字符
    分析：实质就是将十进制转化成26进制
        如果出现了0, 但是我们26 字母 没有任何一个字母是表示0, 所以我们可以从 商 借一个给余数
    :param num:
    :return:
    """
    answer = ""
    while num:
        num -= 1
        num, remainder = divmod(num, 26)
        # chr()——Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
        answer = chr(remainder + 65) + answer
    return answer


if __name__ == '__main__':
    print(excelSheetColumnTitle(num=28))
