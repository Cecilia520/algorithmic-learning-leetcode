#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MergeTwoSortedLists.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/6 10:41   cecilia      1.0        合并两个链表（类似求两个链表的并集U）
问题描述：将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4


"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(linkedlist1: ListNode, linkedlist2: ListNode)->ListNode:
    """
    合并两个有序链表
    思路分析：

    :param linkedlist1:
    :param linkedlist2:
    :return:
    """
    if linkedlist1 is None:
        return linkedlist2
    if linkedlist2 is None:
        return linkedlist1

    if linkedlist1.val > linkedlist2.val:
        linkedlist2.next = mergeTwoLists(linkedlist1, linkedlist2.next)
        return linkedlist2

    else:
        linkedlist1.next = mergeTwoLists(linkedlist1.next, linkedlist2)
        return linkedlist1
