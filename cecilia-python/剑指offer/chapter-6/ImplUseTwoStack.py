#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ImplUseTwoStack.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/8/4 17:39   cecilia      1.0        使用两个栈实现队列
问题描述：
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Cqueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        """
        队列尾部插入整数
        :param value:
        :return:
        """
        self.stack1.append(value)

    def deleteHead(self) -> int:
        """
        在队列头部删除整数
        :return:
        """
        if self.stack2:
            return self.stack2.pop()
        if not self.stack1:
            return -1
        if self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
