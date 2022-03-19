#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ReplaceSpace.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/14 16:51   cecilia      1.0      替换空格（关键点是字符串不能修改，需要重新定义一个字符串）
问题描述：
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

注意点：
1. 字符串自身不能修改；
2. 不能调用字符串相关的库函数
"""
class Solution:
    def replaceSpace(self, s:str)->str:
        """
        字符空格替换
        :param s:
        :return:
        时间复杂度O（N），空间复杂度O（N）
        """
        if s == "":
            return s
        if s == " ":
            return "%20"
        res = ""
        slist = list(s)
        for i in range(len(slist)):
            if slist[i] == " ":
                res += "%20"
            else:
                res += slist[i]
        return res
if __name__ == '__main__':
    so = Solution()
    s = "Hello World, I am JianZhi Offer."
    s1 = "We are happy."
    print(so.replaceSpace(s=s1))
