#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   FindBinaryTreeMaxDepth-1.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/17 16:48   cecilia      1.0       计算二叉树的最高的深度
问题描述：
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：

给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMaxDepthForBinaryTree(self, root: TreeNode):
        """
        计算二叉树的最大深度
        :param root:
        :return:
        时间复杂度：O（N）；空间复杂度O（N）
        """
        if not root:
            return 0
        leftH = 0
        rightH = 0
        if root.left:
            leftH = self.maxDepth(root.left)
        if root.right:
            rightH = self.maxDepth(root.right)
        return max(leftH, rightH) + 1


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = 9
    root.right = 20

    s = Solution()
    print(s.findMaxDepthForBinaryTree(root=root))
