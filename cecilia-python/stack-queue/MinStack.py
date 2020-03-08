#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MinStack.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/7 22:11   cecilia      1.0         最小栈
问题描述：
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

参考解答：https://leetcode-cn.com/problems/min-stack/solution/shi-yong-fu-zhu-zhan-tong-bu-he-bu-tong-bu-python-/

思路分析：
   可以设计两个栈，一个数据栈，一个辅助栈，在代码实现的时候有两种方式：
    1、辅助栈和数据栈同步（极力推荐）
    特点：编码简单，不用考虑一些边界情况，就有一点不好：辅助栈可能会存一些“不必要”的元素。
    算法分析：时间复杂度O(N),空间复杂度O(1)
    2、辅助栈和数据栈不同步
    特点：由“辅助栈和数据栈同步”的思想，我们知道，当数据栈进来的数越来越大的时候，我们要在辅助栈顶放置和当前辅助栈顶一样的元素，这样做有点“浪费”。
    算法分析：时间复杂度O(1),空间复杂度O(N)

同步方法小结：
    出栈时，最小值出栈才同步；入栈时，最小值入栈才同步。
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 数据栈
        self.data = []
        self.helper = []

    def push(self, x: int) -> None:
        """
        入栈
        :param x:
        :return:
        """
        # 向数据栈里面添加元素
        self.data.append(x)
        # 如果当前辅助栈中没有元素或者当前元素比栈顶的元素还要小，那么可以往辅助栈中继续辅助栈中添加元素
        if len(self.helper) == 0 or x < self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])


    def pop(self) -> None:
        """
        出栈
        :return:
        """
        # 只有最小元素才能出栈
        if self.data:
            self.helper.pop()
            return self.data.pop()


    def top(self) -> int:
        """
        获得栈顶元素
        :return:
        """
        if self.data:
            return self.data[-1]

    def getMin(self) -> int:
        """
        get min element.
        :return:
        """
        if self.helper:
            return self.helper[-1]
