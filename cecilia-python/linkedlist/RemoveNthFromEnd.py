#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   RemoveNthFromEnd.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/7 11:54   cecilia      1.0         None
问题描述：
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head: ListNode, n: int)->ListNode:
    """
    解决方案：双指针
        1.添加一个哑结点作为辅助，该结点位于列表头部。
        哑结点用来简化某些极端情况，例如列表中只含有一个结点，或需要删除列表的头部。
        2.分别设定两个间隔为n的快慢指针，fast和slow；
        3.快慢指针同时遍历，当快指针的next达到链表终点，那么慢指针的next就是所要删除的节点
    :param head:
    :return:
    算法分析：时间复杂度O(L),空间复杂度O(1)
    """
    tmp = ListNode(0)
    tmp.next = head # 哑节点指向链表的头节点

    fast, slow = tmp, tmp

    # 快指针先走n步
    for i in range(n):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return tmp.next




