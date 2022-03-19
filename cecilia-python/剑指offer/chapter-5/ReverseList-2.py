#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ReverseList-2.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/14 16:48   cecilia      1.0       反转链表（递归）
问题描述：
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
'''
该题反转链表和将链表从尾到头打印链表的含义还是不太一样的，一般先绘制图然后使用双指针
'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def ReverseList(self, head: ListNode)->ListNode:
        """
        反转链表
        :param head:
        :return:
        复杂度分析：时间复杂度O（），空间复杂度O（1）
        """
        if not head or not head.next:
            return head
        cur, pre = None, head
        while pre:
            # pre.next = cur
            # cur = pre
            # pre = pre.next #继续向前遍历反转
            # 注意： 单值和多值赋值的结果不一样：多值可以同时改变变量的值，单值每次只能改变一个！！！
            pre.next, cur, pre = cur, pre, pre.next

        return cur
if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(7)
    s = Solution()
    print(s.ReverseList(head=head))
