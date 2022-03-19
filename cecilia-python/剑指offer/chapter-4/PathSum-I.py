#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PathSum-I.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/29 17:47   cecilia      1.0      根据指定值找出所有二叉树满足条件的路径列表（递归）
问题描述：
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

 示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def PathSum(self, root: TreeNode, target: int)->List[List[int]]:
        """
        根据指定值找出所有二叉树满足条件的路径列表（递归）
        :param root:
        :param target:
        :return:
        """
        res = []
        path = []
        def recur(root, target):
            if not root: return
            path.append(root.val)
            target -= root.val
            if target == 0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, target)
            recur(root.right, target)
            path.pop()
        recur(root, target)
        return res