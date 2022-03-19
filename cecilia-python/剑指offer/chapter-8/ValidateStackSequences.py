#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ValidateStackSequences.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/9/3 12:49   cecilia      1.0        验证合法的栈序列
问题描述
Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

 

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-stack-sequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # 思路：使用一个辅助栈
        if not pushed and not popped:
            return True
        tmp_stack = []
        j = 0
        for it in pushed:
            tmp_stack.append(it)
            # 如果临时栈中存有元素，并且临时栈的栈顶元素等于出栈的栈顶元素，那么临时栈和出栈的栈同时取出元素
            while tmp_stack and j < len(popped) and tmp_stack[-1] == popped[j]:
                tmp_stack.pop()
                j += 1
        return 0 == len(tmp_stack)


if __name__ == '__main__':
    s = Solution()
    print(s.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]))
