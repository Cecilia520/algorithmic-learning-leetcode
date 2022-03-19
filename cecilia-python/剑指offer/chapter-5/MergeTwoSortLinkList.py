#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MergeTwoSortLinkList.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/24 15:09   cecilia      1.0        合并两个有序的链表
问题描述：
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None
class Solution:
    def mergeTwoSortedLinkedList(self, l1: LinkedList, l2: LinkedList)->LinkedList:
        """
        合并两个有序的链表
        方法：双指针法
        :param l1:
        :param l2:
        :return:
        复杂度分析：时间复杂度O（M+N），空间复杂度O（1）
        """
        if not l1 and l2:
            return l2
        if not l2 and l2:
            return l1
        dum = LinkedList(0)
        cur = dum
        while l1 and l2:
            if l1.val > l2.val:
                cur.next, l2 = l2, l2.next
            else:
                cur.next, l1 = l1, l1.next
            cur.next = cur
        cur.next = l1 if l1 else l2
        return dum.next