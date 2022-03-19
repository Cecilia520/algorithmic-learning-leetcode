#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MaxQueue-II.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/8/11 16:29   cecilia      1.0       最大队列值
问题描述：
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：

输入:
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
示例 2：

输入:
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
'''
主要目的是考察：单调队列！！！
'''
import queue
class MaxQueue:
    def __init__(self):
        self.deque = queue.deque()
        self.queue = queue.Queue()

    def max_vlaue(self)->int:
        # 双端队列的顶部元素即时最大值
        return self.deque[0] if self.deque else -1

    def push_back(self, value:int)->int:
        # 维护一个双端单调队列
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)

    def pop_front(self)->int:
        if not self.deque:
            return -1
        res = self.queue.get()
        if res == self.deque[0]:
            self.deque.popleft()
        return res
