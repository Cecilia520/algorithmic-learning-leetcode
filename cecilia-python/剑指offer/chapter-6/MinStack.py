#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MinStack.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/8/20 13:30   cecilia      1.0       最小栈
问题描述：
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

 

示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class MinStack:
    """
    实现最小栈
    时间复杂度：O（1），空间复杂度O（N）
    """
    def __init__(self):
        self.A = []
        self.B = []

    def push(self, x)->int:
        self.A.append(x)
        if not self.B or self.B[-1] >= x:
            self.B.append(x)

    def pop(self)->int:
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    def top(self)->int:
        return self.A[-1]

    def min(self)->int:
        return self.B[-1]
