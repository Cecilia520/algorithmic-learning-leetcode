#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ImplementStackusingQueues.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/7 22:10   cecilia      1.0         用队列实现栈
问题描述：
使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空
注意:

你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。


思路分析：使用两个栈实现队列
使用两个栈，一个栈（stackPush）用于元素进栈，一个栈（stackPop）用于元素出栈；
1. 入队。一个队列是 FIFO 的，但一个栈是 LIFO 的。这就意味着最新压入的元素必须得放在栈底。
    为了实现这个目的，我们首先需要把 s1 中所有的元素移到 s2 中，接着把新元素压入 s2。
    最后把 s2 中所有的元素弹出，再把弹出的元素压入 s1。

2. 出队。
    如果 stackPop 里面有元素，直接从 stackPop 里弹出或者 peek 元素；
    如果 stackPop 里面没有元素，一次性将 stackPush 里面的所有元素倒入 stackPop。
    注意：一定要保证 stackPop 为空的时候，才能把元素从 stackPush 里拿到 stackPop 中。

算法分析：压入O(1),压出O(n)
"""
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackPop = [] # 用于入队
        self.stackPush = [] # 用于出队


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # 队列的入队操作
        self.stackPop.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return

        # 必须在stackpush中没有元素才能入队，有元素时弹出
        if len(self.stackPush) == 0:
            while len(self.stackPop) != 0:
                self.stackPush.append(self.stackPop.pop())
            return self.stackPush.pop()
        else:
            return self.stackPush.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return

        # 必须在stackpush中没有元素才能入队，有元素时弹出
        if len(self.stackPush) == 0:
            while len(self.stackPop) != 0:
                self.stackPush.append(self.stackPop.pop())
            return self.stackPush[-1]
        else:
            return self.stackPush[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.stackPop) == 0 and len(self.stackPush) == 0:
            return True
        else:
            return False
