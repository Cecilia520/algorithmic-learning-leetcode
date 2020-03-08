#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ValidParentheses.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/7 22:11   cecilia      1.0        括号匹配问题
问题描述：
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

思路参考：https://leetcode-cn.com/problems/valid-parentheses/solution/you-xiao-de-gua-hao-by-leetcode/

算法：
- 初始化栈 S。
- 一次处理表达式的每个括号。
- 如果遇到开括号，我们只需将其推到栈上即可。这意味着我们将稍后处理它，让我们简单地转到前面的 子表达式。
- 如果我们遇到一个闭括号，那么我们检查栈顶的元素。如果栈顶的元素是一个 相同类型的 左括号，那么我们将它从栈中弹出并继续处理。否则，这意味着表达式无效。
- 如果到最后我们剩下的栈中仍然有元素，那么这意味着表达式无效。

算法分析：时间复杂度O(N),空间复杂度O(N)
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 初始化栈
        stack = []

        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:

            # 如果当前字符串是闭括号，那么比较栈顶的元素
            if char in mapping:
                # 如果栈顶元素是同类型的匹配的括号，那么将从栈中弹出
                if stack:
                    top_element = stack.pop()
                else:
                    '#'
                # 不匹配的话，返回False
                if mapping[char] != top_element:
                    return False
                else:
                    # 如果是开括号，那么直接压入栈中
                    stack.append(char)

            # 如果最后栈是空的，那么我们检测的括号匹配存在问题
            return not stack
