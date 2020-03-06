#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ReverseLinkedList.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/6 10:41   cecilia      1.0         反转链表
问题描述：反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseLinkedList(head: ListNode)->ListNode:
    """
    反转一个链表
    思路分析：
         在遍历列表时，将当前节点的 next 指针改为指向前一个元素。由于节点没有引用其上一个节点，因此必须事先存储其前一个元素。
         在更改引用之前，还需要另一个指针来存储下一个节点。
    :param head:
    :return:
    """
    prev, curr = None, head

    while curr != None:
        nextTmp = curr.next
        curr.next = prev
        prev = curr
        curr = nextTmp
    return prev
