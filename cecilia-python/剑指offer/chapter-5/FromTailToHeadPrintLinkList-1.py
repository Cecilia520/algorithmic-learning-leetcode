#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   FromTailToHeadPrintLinkList-1.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/14 16:46   cecilia      1.0       从尾到头打印链表
问题描述：
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
示例 1：

输入：head = [1,3,2]
输出：[2,3,1]
"""
'''
该题主要是考察递归，从尾到头打印链表，并返回值数组，
1.解决思路是就是先遍历到链表末端，然后递归时将值加入list，倒序输出；
2.辅助栈
遍历链表时将值入栈，再出栈即可
'''


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def ReverseLinklist(self, head: ListNode):
        """
        从尾到头打印链表
        思路一：递归法
        :param head:
        :return:
        时间复杂度：O（N），空间复杂度O（N）
        """
        return self.ReverseLinklist(head.next) + [head.val] if head else []

    def ReverseLinklistByStack(self, head: ListNode):
        """
        从尾到头打印链表
        思路一：辅助栈
        :param head:
        :return:
        时间复杂度：O（N），空间复杂度O（N）
        """
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    s = Solution()
    print(s.ReverseLinklist(head=head))
    print(s.ReverseLinklistByStack(head=head))
