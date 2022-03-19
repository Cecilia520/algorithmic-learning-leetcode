#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   HasSubtree.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/15 17:18   cecilia      1.0        判断树A是否是树B的子树
问题描述：
给定两个树，判断是否是子树
注：约定空树不是任意一个树的子结构
"""


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def HasSubtree(T1: TreeNode, T2: TreeNode):
    """
    判断T1是否是T2的子树
    :param T1:
    :param T2:
    :return:
    算法分析：时间复杂度O(NM),空间复杂度O（N），n为树的深度，，
            直接遍历的话，比如先序遍历再比较，时间复杂度是O(M^2+N^2+1),空间复杂度是O(max(m,n))
    """

    def isSubTree(T1: TreeNode, T2: TreeNode):
        if T1 is None:
            return True
        if T2 is None or T1.val != T2.val:
            return False
        return isSubTree(T1.left, T2.left) and isSubTree(T1.right, T2.right)

    if T1 is None or T2 is None:
        return False

    return isSubTree(T1, T2) or HasSubtree(T1.left, T2) or HasSubtree(T1.right, T2)