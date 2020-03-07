#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   AddTwoNumbersII.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/7 12:03   cecilia      1.0         计算链表相加
问题描述：
给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

进阶:
如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

示例:
输入: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出: 7 -> 8 -> 0 -> 7

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    计算两个链表的加法运算
    - @关键点：
        1. 两数相加由于是从低位加到高位，需要从`最后的节点`开始，可以想到用`栈`来解决
    - @思路：
        1. 先将两个链表的每个值存入栈中，然后将每个栈中对应位置的节点相加
        2. 进位通过一个变量保存，每次迭代都将该值加上
    - @注意点：
        1. 创建链表时，要用 `头插法`，否则链表是反的
        2. 判断迭代是否可以继续时，要注意当进位值存在时也需要继续，因为可能出现两个栈都空但存在进位的情况
    :param l1:
    :param l2:
    :return:
    算法分析：时间复杂度和内存都比较高，超出时间和内存限制
    """
    s1 = []
    s2 = []

    # 根据链表创建两个栈,将数据都存储在栈中
    while l1:
        s1, l1 = s1 + [l1.val], l1.next
    while l2:
        s2, l2 = s2 + [l2.val], l2.next

    tmpNode = ListNode(-1)
    carry = 0  # 保存进位的值

    # 若栈不为空或者进位不为空，那么继续迭代
    while s1 or s2 or carry:
        n1, n2 = 0, 0
        if s1:
            n1 = s1.pop() or 0
        if s2:
            n2 = s2.pop() or 0

        # 计算值相加
        count = carry + n1 + n2

        # 需要存入新链表的值
        n = count % 10

        # 使用头插法创建新链表
        newListNode = ListNode(n)
        newListNode.next = tmpNode.next
        tmpNode.next = newListNode

        carry = int(count / 10)

    return tmpNode.next


def addTwoNumbers1(l1: ListNode, l2: ListNode) -> ListNode:
    """
    优化方案：递归解决（时间优化很多）
        1. 计算两个链表长度
        2. 递归 计算每一位数字 分情况处理 链表 i，j 长度 num_i,num_j
        3. 高位（长链表 多出的位数 即 num_i > num_j的部分）= i.val + 下一位进位
        4. 等长部分 = i.val + j.val + 下一位进位
        5. 计算 进位，更新 i.val (以长链表作最终结果)
        6. 最后注意 头节点的进位，判断需不需要加一个头节点
    :param l1:
    :param l2:
    :return:
    """
    def add(n1, n2, i, j):
        """
        值求和
        :param n1:l1链表的长度
        :param n2:l2链表的长度
        :param i:
        :param j:
        :return:
        """
        if not i or not j:
            return 0

        if n1 > n2:
            temp = i.val + add(n1 - 1, n2, i.next, j)
        else:
            temp = i.val + add(n1, n2, i.next, j.next)

        i.val = temp % 10 #
        return temp // 10

    n1, n2 = 0, 0
    cur = l2
    while cur:
        n2 += 1

    cur = l1
    while cur:
        n1 += 1

    # 比较两个表的长度,如果当前n2要长，那么交换两个链表
    if n2 > n1:
        l1, l2 = l2, l1
        n2, n1 = n1, n2

    # 严格要求长链表加短链表
    if add(n1, n2, l1, l2):
        l2 = ListNode(1)
        l2.next = l1
        l1 = l2
    return l1




