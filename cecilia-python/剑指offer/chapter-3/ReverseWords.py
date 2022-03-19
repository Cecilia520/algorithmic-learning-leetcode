#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ReverseWords.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/17 17:22   cecilia      1.0       翻转单词的顺序
问题描述：
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。

示例 1：

输入: "the sky is blue"
输出: "blue is sky the"
示例 2：

输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：

输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
 
说明：
1.无空格字符构成一个单词。
2.输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
3.如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
'''
该题的考点：
1. 栈
2. 双指针

思路：
1. 直接倒序遍历字符串
2. 先进后出
'''

class Solution:
    def ReverseWords(self, word):
        """
        翻转单词
        :param word:
        :return:
        时间复杂度O（N），空间复杂度O（1）
        """
        if not word:
            return None
        if word == "":
            return word
        word_list = list(word.strip().split())
        res = ""
        for i in range(len(word_list) - 1, -1, -1):
            res += " " + word_list[i]
        return res

    def ReverseWordsByStack(self, word):
        """
        使用栈解决方案
        :param word:
        :return:
        """
        wordlist = word.strip().split()
        stack = []

        res = ""
        for wl in wordlist:
            stack.append(wl)
        for i in range(len(stack)-1, -1, -1):
            res += stack[i] + " "
        return res




if __name__ == '__main__':
    s = Solution()
    word = "blue. is sky the"
    # print(s.ReverseWords(word=word))
    print(s.ReverseWordsByStack(word=word))

