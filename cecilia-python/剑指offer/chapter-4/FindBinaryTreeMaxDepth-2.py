#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   FindBinaryTreeMaxDepth-1.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/17 16:48   cecilia      1.0      判断是否是平衡二叉树
问题描述：
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。
如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

示例 1:
给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isBalance(self, root: TreeNode) -> bool:
        """
        判断当前二叉树是否是平衡二叉树
        关键点：先计算二叉树的最大深度，如果二叉树的左右子树存在，那么左右子树的高度相差不等于1，即可判断是平衡二叉树
        :param root:
        :return:
        时间复杂度：O（N）；空间复杂度O（N）
        """
        if not root:
            return True  # 空树也是平衡二叉树

        def isBalanceByRoot(root):
            if not root:
                return 0
            left_h, right_h = 0, 0
            if root.left:
                left_h = isBalanceByRoot(root.left)
                if left_h == -1:
                    return -1
            if root.right:
                right_h = isBalanceByRoot(root.right)
                if right_h == -1:
                    return -1
            return max(right_h, left_h) + 1 if abs(left_h - right_h) <= 1 else -1

        return isBalanceByRoot(root) != -1

