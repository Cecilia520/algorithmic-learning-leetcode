#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   SymmetricTree.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/10 21:12   cecilia      1.0        镜像对称树
问题描述：
给定一个二叉树，判断是对称镜像树
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSymmetricTree(root: TreeNode):
    """
    判断是否是镜像对称树
    思路：递归 + 迭代
        将镜像树看作是两个树，左子树和对方的右子树相同，右子树和左子树相同（空树也是对称树）
    :param root:
    :return:
    """

    def isSymmetricTreeWithRoot(T1: TreeNode, T2: TreeNode):
        """
        递归判断两个树
        :param T1:
        :param T2:
        :return:
        算法分析：时间复杂度O(N)，空间复杂度O(N)
        """
        if T1 is None and T2 is None:
            return True
        if T1 is None or T2 is None:
            return False

        if T1 and T2 and T1.val != T2.val:
            return False

        return isSymmetricTreeWithRoot(T1.left, T2.right) and isSymmetricTreeWithRoot(T1.right, T2.left)

    if root is None:
        return True

    return isSymmetricTreeWithRoot(root.left, root.right)
