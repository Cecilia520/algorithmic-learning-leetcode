#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   InvertBinaryTree.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/10 21:10   cecilia      1.0       翻转二叉树
问题描述：
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

"""
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def invertBinaryTree(root: TreeNode)->TreeNode:
    """
    翻转二叉树
    思路分析：右子树和左子树进行交换
    :param root:
    :return:
    """
    if root is None:
        return None
    left = root.left
    root.left = invertBinaryTree(root.right)
    root.right = invertBinaryTree(left)
    return root

