#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   22.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/11 21:01   cecilia      1.0         None
"""
#
# 对给定的二叉树依次完成前序，中序，后序遍历，并输出遍历结果
# @param input int整型一维数组 -1表示Nil节点
# @return int整型二维数组
#
class Solution:
    def preorderTraverse(self, root):
        """
        前序遍历 【根左右】
        """
        if not root:
            return None
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if root.right:
                stack.append(node.right)
            if root.left:
                stack.append(node.left)
            res.append(node.val)
        return res
    def inorderTraverse(self, root):
        """
        中序遍历 【左根右】
        """
        if not root:
            return None
        stack = [(1, root)]
        res = []
        while stack:
            flag, node = stack.pop()
            if flag == 0:
                res.append(node.val)
            else:
                if node.right:
                    stack.append((1, node.right))
                stack.append((0,node))
                if node.left:
                    stack.append((1, node.left))
        return res
    def postorderTraverse(self, root):
        """
        后序遍历 【左右根】
        """
        if not root:
            return None
        stack = [(1, root)]
        res = []
        while stack:
            flag, node = stack.pop()
            if flag == 0:
                res.append(node.val)
            else:
                stack.append((0, node))
                if node.right:
                    stack.append((1, node.right))
                if node.left:
                    stack.append((1, node.left))
        return res
    def binaryTreeScan(self , input ):
        # write code here
        result = []
        if not input:
            return None
        result.append(self.preorderTraverse(input))
        result.append(self.inorderTraverse(input))
        result.append(self.postorderTraverse(input))
        return result
