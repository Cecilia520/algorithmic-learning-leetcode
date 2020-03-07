#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   SplitLinkedListinParts.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/7 13:37   cecilia      1.0         分割链表
问题描述：
给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。

每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。

这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。

返回一个符合上述规则的链表的列表。

举例： 1->2->3->4, k = 5 // 5 结果 [ [1], [2], [3], [4], null ]

示例 1：

输入:
root = [1, 2, 3], k = 5
输出: [[1],[2],[3],[],[]]
解释:
输入输出各部分都应该是链表，而不是数组。
例如, 输入的结点 root 的 val= 1, root.next.val = 2, \root.next.next.val = 3, 且 root.next.next.next = null。
第一个输出 output[0] 是 output[0].val = 1, output[0].next = null。
最后一个元素 output[4] 为 null, 它代表了最后一个部分为空链表。
示例 2：

输入:
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
输出: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
解释:
输入被分成了几个连续的部分，并且每部分的长度相差不超过1.前面部分的长度大于等于后面部分的长度。

"""
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def splitLinkedListinParts(root: ListNode, k: int) -> List[ListNode]:
    """
    将链表分割成k个链表集合
    思路：拆分链表。
        1.如果链表有 N 个结点，则分隔的链表中每个部分中都有 n/k 个结点，且前 N%k 部分有一个额外的结点。
        2.可以用一个简单的循环来计算 N。对于每个部分，已经计算出该部分有多少个节点：width + (i < remainder ? 1 : 0)
        3.直接拆分原链表，并根据需要返回指向原始链表中节点的指针列表。
    :return:
    算法分析：时间复杂度O(N+K),空间复杂度O(K)
    """
    cur = root
    # 题目要求大小是[0,1000]
    for N in range(1001):
        if not cur:
            break
        cur = cur.next
    width, remainder = divmod(N, k)

    ans = []
    cur = root
    for i in range(k):
        head = cur
        for j in range(width+(i < remainder) - 1):
            if cur:
                cur = cur.next
        if cur:
            cur.next, cur = None, cur.next
        ans.append(head)
    return ans



