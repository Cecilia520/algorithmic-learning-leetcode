#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   SumofLeftLeaves.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/10 21:13   cecilia      1.0       统计左右子节点的和
问题描述：
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-left-leaves
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def getSumofLeftLeaves(root:TreeNode)->int:
    if not root:
        return 0

    def isLeftLeaf(root):
        # 判断是否是叶子节点
        if root is None:
            return False
        return root.left is None and root.right is None

    if isLeftLeaf(root.left):
        return root.left.val + getSumofLeftLeaves(root.right)

    return getSumofLeftLeaves(root.left) + getSumofLeftLeaves(root.right)

