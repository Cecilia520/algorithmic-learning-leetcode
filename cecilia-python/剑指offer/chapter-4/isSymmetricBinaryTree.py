#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   isSymmetricBinaryTree.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/22 17:29   cecilia      1.0       是否是对称二叉树（递归）
问题描述：
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isSymmetricBinaryTree(self, root: TreeNode) -> bool:
        """
        判断是否是对称二叉树（如果一棵二叉树和镜像树是相等的，那么此二叉树是对称的）
        此处可以将二叉树的左右子树作为一个镜像，左子树的根节点的值和右子树的根结点的值是否相等，左子树和右子树的值对应是否相等
        :param root:
        :return:
        复杂度分析：时间复杂度O（N）,空间复杂度O（N），当二叉树退化为链表，系统使用 O(N) 大小的栈空间
        """

        def isSymmetricBinaryTreeByRoot(L, R):
            if not L and not R:
                return True
            if not L or not R or L.val != R.val:
                return False
            return isSymmetricBinaryTreeByRoot(L.left, R.right) and isSymmetricBinaryTreeByRoot(L.right, R.left)

        if not root:
            return True
        return isSymmetricBinaryTreeByRoot(root.left, root.right)
