#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ReverseString.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/16 10:58   cecilia      1.0      反转字符串中的元音字母

题目描述：编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
示例：Given s = "leetcode", return "leotcede".
"""
def reverseVowels(s: str)->str:
    """
    反转一个字符串中的元音字母
    解题思路：输入一个字符串，然后采用双指针分别进行从头和从尾部进行遍历和判断。
    如果是元音字母，则作为索引结果，相互调换位置，否则继续搜索。
    :param s:输入的字符串
    :return:str
    算法分析：时间复杂度O(N,空间复杂度O(1)
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    strlist = list(s)
    if s is None:
        return None
    i, j = 0, len(s) - 1
    while i <= j:
        if strlist[i] not in vowels:  # Java中可以直接使用字符串的chartAi(index)得到相应的字符，然后根据字符串的contains(charti)的方法判断是否是元音字母
            i = i + 1
        elif strlist[j] not in vowels:
            j = j - 1
        elif strlist[i] in vowels and strlist[j] in vowels:
            strlist[i], strlist[j] = strlist[j], strlist[i]
            i = i + 1
            j = j - 1
    return "".join(strlist)



if __name__ == '__main__':
    s = "lEEtcOdE"
    print(reverseVowels(s))

