#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ImplementQueueusingStacks.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/7 22:10   cecilia      1.0         用栈实现队列
问题描述：
使用栈实现队列的下列操作：

push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。
示例:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false

思路分析：
涉及两个队列，一个队列入栈，另一个出栈
"""
from collections import deque

class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dequePop = deque()
        self.dequePush = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.dequePop.append(x) # 直接入队

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        # 如果队列中存有元素，直接弹出到另一个队列中
        while len(self.dequePop) > 1:
            self.dequePush.append(self.dequePop.popleft()) # 从左边删除元素
        tmp = self.dequePop.popleft()
        self.dequePop, self.dequePush = self.dequePush, self.dequePop
        return tmp


    def top(self) -> int:
        """
        Get the top element.
        """
        while len(self.dequePop) != 1:
            self.dequePush.append(self.dequePop.popleft())
        tmp = self.dequePop.popleft()
        self.dequePush.append(tmp)
        self.dequePush, self.dequePop = self.dequePop, self.dequePush
        return tmp

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.dequePop) == 0

