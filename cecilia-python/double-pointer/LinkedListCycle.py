#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   LinkedListCycle.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/16 16:08   cecilia      1.0      判断链表是否存在环
题目描述：给定一个链表，判断链表中是否有环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：

输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
参考地址：https://leetcode-cn.com/problems/linked-list-cycle/solution/dong-hua-yan-shi-141-huan-xing-lian-biao-by-user74/
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def LinkedListCycle(head: ListNode, pos: int) -> bool:
    """
    判断链表中是否存在环
    :param head:头部
    :param pos:链表索引位置，如果pos=-1，表示连接尾部，此时可以认为是没有环
    :return: 是否存在环
    快慢双指针：
    - 设两指针fast slow指向链表头部head，迭代：
        fast每轮走两步，slow每轮走一步，这样两指针每轮后距离+1;
    - 若链表中存在环，fast和slow一定会在将来相遇（距离连续+1，没有跳跃）；
    - 若fast走到了链表尾部，则说明链表无环。

    算法分析：时间复杂度O(n),空间复杂度O(1)
    """
    #如果没有头指针，说明此链表无环
    if not(head and head.next):
        return False
    #定义双指针，一个快指针，一个慢指针，快指针的速度是慢指针的一倍
    slow, fast = head, head.next
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False

# 获得相遇的点
def _get_meet_Node(head):
    if head is None or head.next is None:
        return None
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow
    return None


# 获得环入口的节点
def get_Loop_Node(head, meetNode):
    first = head
    second = meetNode
    while first != second:
        first = first.next
        second = second.next


if __name__ == '__main__':
    # linknode1 = ListNode(3)
    # linknode2 = ListNode(2)
    # linknode3 = ListNode(0)
    # linknode4 = ListNode(-4)
    # linknode2 = linknode1.next
    # linknode3 = linknode2.next
    # linknode4 = linknode3.next
    # head = linknode1.val
    # print(linknode1.val)
    # head =
    head = [3, 2, 0, -4]
    pos = 0
    print(LinkedListCycle(head, pos)) # False


