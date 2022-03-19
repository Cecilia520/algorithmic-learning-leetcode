#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MergeTwoBinaryTrees.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/10 21:10   cecilia      1.0        合并两个树
问题描述：
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

示例 1:

输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
注意: 合并必须从两个树的根节点开始。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-binary-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
def mergeTree(t1:TreeNode, t2:TreeNode)->TreeNode:
    """
    合并两个树——递归，值相加，子树合并
    :param t1:
    :param t2:
    :return:
    """
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    if t1 is None and t2 is None:
        return None

    root = TreeNode(t1.val + t2.val)
    root.left = mergeTree(t1.left, t2.left)
    root.right = mergeTree(t1.right, t2.right)
    return root
