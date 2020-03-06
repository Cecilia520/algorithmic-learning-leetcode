#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   IntersectionofTwoLinkedLists.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/6 10:40   cecilia      1.0         相交链表
问题描述：编写一个程序，找到两个单链表相交的起始节点。

如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

"""
from Cython.Compiler.ExprNodes import ListNode


def getIntersectionNode(headA: ListNode, headB: ListNode):
    """
    获取两个链表的相交节点
    思路分析：
        方法一：直接遍历法
            对链表A中的每一个结点ai，遍历整个链表 B并检查链表 B中是否存在结点和 ai相同。
        算法分析：时间复杂度O(mn),空间复杂度O(1)

        方法二：双指针法(推荐)
            设定两个指针分别指向两个链表头部，一起向前走直到其中一个到达末端，另一个与末端距离则是两链表的 长度差。
            再通过长链表指针先走的方式消除长度差，最终两链表即可同时走到相交点。
        算法分析：时间复杂度O(m+n)，空间复杂度O（1）
    :param headA: 一个链表
    :param headB: 另一个链表
    :return:
    """
    ha, hb = headA, headB
    while ha != hb:
        ha = ha.next if ha else headB
        hb = hb.next if hb else headA
    return ha