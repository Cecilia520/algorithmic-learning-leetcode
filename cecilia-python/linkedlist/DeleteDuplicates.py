#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   DeleteDuplicates.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/7 11:26   cecilia      1.0       删除链表中重复的结点
问题描述：给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplicates(head: ListNode)->ListNode:
    """
    删除链表中重复的节点
    思路：递归删除
    :param head:
    :return:
    算法分析：时间复杂度O(N),空间复杂度O(1)
    """
    if head is None or head.next is None:
        return head

    head.next = deleteDuplicates(head.next)

    if head.val == head.next.val:
        return head.next
    else:
        return head
