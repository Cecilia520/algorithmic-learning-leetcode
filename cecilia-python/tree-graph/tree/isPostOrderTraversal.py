#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   isPostOrderTraversal.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/17 17:25   cecilia      1.0       判断当前的序列是否是后序遍历
问题描述：
给定一个整数序列，判断是否是某个二叉树的后序遍历

思路分析：
    首先是后序遍历，那么序列的最后一个元素是根节点，然后根据根节点判断左子树的长度和右子树的长度序列，
    接着根据二叉树的特点，左子树所有节点值小于根节点，右子树的所有节点值大于根节点，
    最后根据左右子树递归判断下去
依据：
BST的后序序列的合法序列是，对于一个序列S，最后一个元素是x （也就是根），如果去掉最后一个元素的序列为T，
那么T满足：T可以分成两段，前一段（左子树）小于x，后一段（右子树）大于x，且这两段（子树）都是合法的后序序列。

前序遍历：根 > 左 > 右
中序遍历： 左 > 根 > 右
>> 假设二叉排序树的定义是：
1、若它的左子树不为空，则左子树所有节点均小于它的根节点的值；
2、若右子树不为空，则右子树所有节点的值均大于根节点的值；
3、它的左右子树也分别为二叉排序树
"""
def isPostOrderTraversal(sequence):
    """
    根据给定的序列，判定是否某个二叉树的后序遍历
    :param sequence:
    :return:
    """
    if len(sequence) < 0 or sequence is None:
        return False
    L = len(sequence)

    if L == 1:
        return True

    # 确定根节点
    root = sequence[-1]

    # 获得左子树的index
    index = 0
    while sequence[index] < root:
        index += 1

    # 判断右子树
    for i in range(index, L-1):
        if sequence[i] < root:
            return False

    # 左右子树序列
    left = sequence[:index]
    right = sequence[index:L-1]

    isLeft, isRight = True, True
    if len(left) > 0:
        isLeft = isPostOrderTraversal(left)

    if len(right) > 0:
        isRight = isPostOrderTraversal(right)

    return isLeft and isRight

