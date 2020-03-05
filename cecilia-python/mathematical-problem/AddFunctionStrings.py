#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   AddFunctionStrings.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/3 19:04   cecilia      1.0         字符串加法运算
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。

算法思路：双指针法
"""
def addFunctionStrings(num1, num2):
    """
    参考：链接：https://leetcode-cn.com/problems/add-strings/solution/add-strings-shuang-zhi-zhen-fa-by-jyd/
    双指针法：
       1. 设置两个指针，分别指向两个num1和num2的尾部；
       2. 计算进位。如果当前位计算的值设定为tmp=num1+num2, carry=tmp//10大于等于0，当前需要进位，否则不需要；
       3. 添加当前位。计算tmp=num1+num2+carry,并将个位数添加到头部；
       4. 索引溢出处理： 当指针 i或j 走过数字首部后，给 n1，n2 赋值为 00，相当于给 num1，num2 中长度较短的数字前面填 00，以便后续计算。
       5. 当遍历完 num1，num2 后跳出循环，并根据 carry 值决定是否在头部添加进位 11，最终返回 res 即可。
    :param num1:
    :param num2:
    :return:
    算法分析：时间复杂度O（max(M,N)）,空间复杂度O(max(M,N))
    """
    i, j = len(num1)-1, len(num2)-1
    carry = 0
    result = ""
    while i >= 0 or j >= 0:
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0
        tmp = n1 + n2 + carry
        # 判断是否进位
        carry = tmp // 10
        result = str(tmp % 10) + result
        i, j = i - 1, j - 1
    return "1" + result if carry else result

if __name__ == '__main__':
    print(addFunctionStrings(num1="51189", num2="967895"))