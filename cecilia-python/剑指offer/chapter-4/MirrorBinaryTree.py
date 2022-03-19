#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MirrorBinaryTree.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/22 17:22   cecilia      1.0      获得二叉树的镜像树
问题描述：
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：
     4
   /   \
  2     7
 / \   / \
1   3 6   9

镜像输出：
     4
   /   \
  7     2
 / \   / \
9   6 3   1

示例 1：
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
'''
镜像二叉树实质上思路就是左右子树数据交换，递归以此类推
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def MirrorBinaryTree(self, root: TreeNode) -> TreeNode:
        """
        二叉镜像树
        :param root:
        :return:
        复杂度分析：时间复杂度O（n），空间复杂度O(n)
        """
        if not root:
            return
        tmp = root.left  # 暂存左子树
        root.right = self.MirrorBinaryTree(root.left)
        root.left = self.MirrorBinaryTree(tmp)
        return root
