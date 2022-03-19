#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PrintTreeFromLeftToRight.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/1 20:16   cecilia      1.0        从左至右打印二叉树
问题描述：
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""
from typing import List


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def printTreeFromLeftToRight(root:TreeNode)->List[List[int]]:
    """
    从左至右打印二叉树
    思路分析：根据depth来决定每一层的高度，从根节点开始遍历，然后遍历下一层，以下一层的左节点和右节点分别为根节点，递归遍历下一层
    :param root:
    :return:
    """
    result = []
    def printTreeWithRoot(root, depth):
        if root:
            if len(result) < depth:
                result.append([])

            result[depth-1].append(root.val)
            printTreeWithRoot(root.left, depth+1)
            printTreeWithRoot(root.right, depth+1)

    printTreeWithRoot(root, 1)
    return result



