#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   FirstUniqChar.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/8/4 14:07   cecilia      1.0         寻找第一次只出现一次的字符
问题描述：
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:

s = "abaccdeff"
返回 "b"

s = ""
返回 " "

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
'''
该题主要考察哈希表，可以采用哈希表存储该字符是否出现次数情况，可以使用普通的哈希表和有序哈希表；
在哈希表的基础上，有序哈希表中的键值对是 按照插入顺序排序 的。基于此，可通过遍历有序哈希表，实现搜索首个 “数量为 11 的字符”。
'''
import collections


class Solution:
    def firstUniqChar(self, s: str) -> str:
        """
        寻找第一次只出现一次的字符（普通哈希表）
        :param s:
        :return:
        复杂度分析：时间复杂度O（N），空间复杂度            hashDict[i] = not i in hashDict
O（N）
        """
        if s == "": return " "
        hashDict = {}
        for i in s:
            hashDict[i] = not i in hashDict
        for k, v in hashDict.items():
            if v:
                return k
        return " "

    def firstUniqCharPlus(self, s: str) -> str:
        """
        寻找第一次只出现一次的字符（普通哈希表）
        :param s:
        :return:
        复杂度分析：时间复杂度O（N），空间复杂度
O（N）
        """
        dic = collections.OrderedDict()
        for i in s:
            dic[i] = not i in dic
        for k, v in dic.items():
            if v: return k
        return " "


if __name__ == '__main__':
    sl = Solution()
    print(sl.firstUniqChar(s="cc"))
