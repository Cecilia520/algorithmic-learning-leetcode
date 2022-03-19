#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   LowestCommonAncestor-I.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/8/19 19:12   cecilia      1.0       二叉树最近公共祖先（注意二叉树的特点，结点不存在特殊性）
问题描述：

"""
'''
思路：递归（后序遍历DFS）
'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def LowestCommonAncestor(self, root:TreeNode, p:TreeNode, q:TreeNode)->TreeNode:
        """
        二叉树的最近公共祖先
        （递归，后序遍历）
        :param root:
        :param p:
        :param q:
        时间复杂度分析：当树退化为链表，O（N）
        :return:
        """
        if not root or root == p or root ==q:
            return root
        left = self.LowestCommonAncestor(root.left, p, q)
        right = self.LowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root


