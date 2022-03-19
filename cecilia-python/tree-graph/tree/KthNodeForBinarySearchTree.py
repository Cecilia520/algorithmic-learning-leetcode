#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   KthNodeForBinarySearchTree.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/1 22:33   cecilia      1.0         查找二叉搜索树的第k个节点的值
问题描述:
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。

思路分析：因为第三个节点是4，而前序遍历5324768，中序遍历2345678，后序遍历2436875，所以是中序遍历，左根右。
因此，首先中序遍历，然后返回第k个节点即可。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.result = []

    def KthNode(self, pRoot, k):
        """
        返回二叉搜索树的第k个节点
        :param pRoot:
        :param k:
        :return:
        """
        # 中序遍历
        def inorderTraversal(root):
            if not root:
                return None
            # 左根右
            inorderTraversal(root.left)
            self.result.append(root)
            inorderTraversal(root.right)

        if not pRoot:
            return None
        inorderTraversal(pRoot)
        if k <= 0 or len(self.result) < k:
            return None
        else:
            return self.result[k - 1]

