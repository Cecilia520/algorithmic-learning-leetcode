#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ConvertNumberToHexadecimal.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/3 19:00   cecilia      1.0         None
给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，通常使用 <补码运算> 方法。

注意:

十六进制中所有字母(a-f)都必须是小写。
十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。 
给定的数确保在32位有符号整数范围内。
不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。

示例 1：
输入:
26

输出:
"1a"

示例 2：
输入:
-1

输出:
"ffffffff"

"""
def convertNumberToHexadecimal(num):
    """
    将一个整数转化成16进制数
    思路：
       对于小于0的数，需要使用补码运算（Python需要自行构造最大整数）；
       对于大于0的数，采用取模16（0x00000010）进行取模，获得商和余数，余数等同于转换字符中的index索引位置；
    :param num:
    :return:
    算法分析：时间复杂度O(logN),空间复杂度O(1)
    """
    # 小于0的数，进行补码运算
    max_int = 0xffffffff + 0x00000001
    if num < 0:
        num += max_int

    hex_convert = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
    divisor = 0x00000010  # 除数
    result = ''  # 结果

    # do-while循环取模运算
    quotient, remainder = divmod(num, divisor)
    result = hex_convert[remainder] + result
    while True:
        quotient, remainder = divmod(quotient, divisor)
        if not (quotient == remainder == 0): #如果都不为0
            result = hex_convert[remainder] + result
        else:
            break

    return result

if __name__ == '__main__':
    print(convertNumberToHexadecimal(num=26))



