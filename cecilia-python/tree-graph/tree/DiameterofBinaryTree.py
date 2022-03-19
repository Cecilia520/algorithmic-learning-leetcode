#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   DiameterofBinaryTree.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/10 21:10   cecilia      1.0       计算树的直径
问题描述：
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。

示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

注意：两结点之间的路径长度是以它们之间边的数目表示。


"""


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterofBinaryTree(self, root: TreeNode):
        """
        思路分析：实际上最大直径就是最大深度减1，经过的路径可以是左右子树浏览经过拼接而成
        :param root:
        :return:
        算法分析：时间复杂度O(N),空间复杂度O(H树的深度)
        """
        self.maxLenth = 1  # 全局变量

        def maxDepth(node: TreeNode) -> int:
            """
            递归判断经过节点数的最大值
            :param node:
            :return:
            """
            if not node:
                return 0

            left = maxDepth(node.left)
            right = maxDepth(node.right)
            # 递归更新找最大长度
            self.maxLenth = max(self.maxLenth, left + right + 1)

            # 最后返回根节点为根的树的深度
            return max(left, right) + 1

        maxDepth(root)
        return self.maxLenth - 1
