#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MaximumDepthofBinaryTree.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/10 21:09   cecilia      1.0         树的高度
问题描述：
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

"""
class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root: TreeNode):
    """
    找二叉树的最大深度
    思路分析：递归（深度优先遍历）
    :param root:
    :return:
    算法分析：时间复杂度是O(N),在最糟糕的情况下，树是完全不平衡的，例如每个结点只剩下左子结点，递归将会被调用 N 次（树的高度），因此保持调用栈的存储将是 O(N)。
          但在最好的情况下（树是完全平衡的），树的高度将是 log(N)。因此，在这种情况下的空间复杂度将是 O(log(N))。
    """
    if root is None:
        return 0
    else:
        left_height = maxDepth(root.left)
        right_height = maxDepth(root.right)
        return max(left_height, right_height) + 1


