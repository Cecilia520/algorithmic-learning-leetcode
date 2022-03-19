#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   BalancedBinaryTree.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/10 21:09   cecilia      1.0        判断当前的树是否是平衡二叉树
问题描述：
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。


"""
class TreeNode:
    def __init__(self, val,left, right):
        self.val = val
        self. left = left
        self.right = right

def isBalancedBinaryTree(root:TreeNode)->bool:
    """
    思路分析：自底向上进行递归判断是否平衡（先计算当前节点的子节点高度，然后再通过子节点高度判断当前节点是否平衡，）
        只有每个节点左右子树高度差不大于 1 时，该树才是平衡的。因此可以比较每个节点左右两棵子树的高度差，然后向上递归。
    :return:
      时间复杂度O(N),空间复杂度O(N)
    """
    def isBalanceHelper(root:TreeNode)->(bool, int):
        """
        判断当前结点的是否平衡
        :param root:
        :return:bool当前子节点高度以及子节点高度的父节点是否平衡
        """
        if root is None:
            return True, -1

        # 分别检查左右子树
        leftBalance, leftHeight = isBalanceHelper(root.left)
        if not leftBalance:
            return False, 0

        rightBalance, rightHeight = isBalanceHelper(root.right)
        if not rightBalance:
            return False, 0

        # 如果左右子树是平衡，那么检查当前结点的树是否是平衡的
        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)

    return isBalanceHelper(root)[0]


