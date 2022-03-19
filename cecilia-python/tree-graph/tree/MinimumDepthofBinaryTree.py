#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MinimumDepthofBinaryTree.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/10 21:12   cecilia      1.0       计算树的最小深度
问题描述：
给定一个二叉树，求取树的最小深度
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def getMinimumDepthofBinaryTree(root:TreeNode)->int:
    """
    计算树的最小深度
    :param root:
    :return:
    算法分析：时间复杂度O(N),最好的情况下是空间复杂度O(logN),最坏的情况时间复杂度是O(N)
    """
    if root is None:
        return 0
    leftHeight = getMinimumDepthofBinaryTree(root.left)
    rightHeight = getMinimumDepthofBinaryTree(root.right)

    if leftHeight == 0 or rightHeight == 0:
        return leftHeight + rightHeight + 1

    return min(leftHeight, rightHeight) +1
