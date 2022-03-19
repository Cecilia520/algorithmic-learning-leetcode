#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PrintTreeFromLeftToRight-II.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/1 21:42   cecilia      1.0        按照“之”形状打印二叉树
问题描述：
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def printTreeFromLeftToRightII(self, pRoot):
    # write code here
    result = []


    def printWithRoot(pRoot, depth):
        if pRoot:
            if len(result) < depth:
                result.append([])
            result[depth-1].append(pRoot.val)
            printWithRoot(pRoot.left, depth + 1)
            printWithRoot(pRoot.right, depth + 1)


    printWithRoot(pRoot, 1)

    for i in range(len(result)):
        if (i & 1) == 1:
            result[i] = result[i][::-1]
    return result
