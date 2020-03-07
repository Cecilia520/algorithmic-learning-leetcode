#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PalindromeLinkedList.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/7 13:36   cecilia      1.0         回文链表
问题描述：
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def palindromeLinkedList(head: ListNode)->ListNode():
    """
    回文链表
    方法一：将链表数据存储在数组中，然后判断是否是回文
    算法分析：时间复杂度O(N)，空间复杂度O(N)
    :param head:
    :return:
    """
    arrVals = []
    cur = head
    while cur:
        arrVals.append(cur.val)
        cur = cur.next
    return arrVals == arrVals[::-1]
