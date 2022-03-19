#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   LowestCommonAncestor-I.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/8/19 19:12   cecilia      1.0       二叉搜索树最近公共祖先（注意二叉搜索树的特点，结点存在特殊性）
问题描述：

"""
'''
递归
思路：
1.如果p，q两个结点的值小于root的值，那么说明两个结点在左子树；
2.如果p，q两个结点的值大于root的值，那么说明两个结点在右子树；
3.否则为root的值
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def LowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        二叉搜索树的最近公共祖先
        （递归）
        :param root:
        :param p:
        :param q:
        时间复杂度分析：当树退化为链表，O（N）
        :return:
        """
        if root.val < p.val and root.val < q.val:
            return self.LowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.LowestCommonAncestor(root.left, p, q)
        return root