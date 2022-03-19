#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   GetIntersectionNode.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/8/20 13:20   cecilia      1.0        两个链表的第一个公共节点
问题描述：
输入两个链表，找出它们的第一个公共节点。

示例 1：


输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def getIntersectionNode(self, headA:ListNode, headB:ListNode)->ListNode:
        """
        获取两个链表的公共交点
        :param headA:
        :param headB:
        :return:
        复杂度分析：时间复杂度O（M+N），空间复杂度O（1）
        """
        node1, node2 = headA, headB
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA
        return node1