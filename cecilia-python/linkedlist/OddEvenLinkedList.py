#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   OddEvenLinkedList.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/7 13:37   cecilia      1.0         链表元素按照奇偶聚集
问题描述：
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

示例 1:

输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL
示例 2:

输入: 2->1->3->5->6->4->7->NULL
输出: 2->3->6->7->1->5->4->NULL

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def oddEvenLinkedList(head: ListNode)->ListNode:
    """
    奇偶聚集
    思路：将奇节点放在一个链表里，偶链表放在另一个链表里。然后把偶链表接在奇链表的尾部。
    算法分析：O(n),空间复杂度O(1)
    :return:
    """
    if head is None:
        return None

    odd = head
    even = head.next
    evenHead = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    # 将偶链表拼接到奇链表后面
    odd.next = evenHead
    return head



