#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ReConstructBinaryTreeForPreAndMiddleTree.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/16 18:13   cecilia      1.0       根据先序遍历和中序遍历构建树
问题描述：
根据先序遍历和中序遍历构建树
思路方法：递归
"""
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
def reConstructBinaryTree(pre:TreeNode, middle:TreeNode):
    """
    根据先序遍历和中序遍历构建树
    :param pre:
    :param middle:
    :return:
    """

