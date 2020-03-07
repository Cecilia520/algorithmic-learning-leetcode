#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   SwapNodesPairs.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/7 12:03   cecilia      1.0         交换两个链表
问题描述：
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def swapNodesPairs(head: ListNode) -> ListNode:
    """
    交换节点
    解决方法：以两个单节点的交换为基础进行递归
    算法分析：时间复杂度O(N);空间复杂度O(1)
    :param head:
    :return:
    """
    if not head or not head.next:
        return head

    nextNode = head.next
    head.next = swapNodesPairs(nextNode.next)
    nextNode.next = head

    return nextNode

