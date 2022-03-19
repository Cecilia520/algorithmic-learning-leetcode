#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PrintBinaryTree-I.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/29 17:53   cecilia      1.0       从上到下打印二叉树
问题描述：
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

 例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

'''
思路分析：
打印二叉树，一般可以采用队列的方式进行存储遍历的数据
'''
import collections

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def printBinaryTree(self, root: TreeNode)->List[int]:
        """
        从上到下打印二叉树
        :param root:
        :return:
        复杂度分析：时间复杂度O（N），空间复杂度O（N）
        """
        if not root:
            return []
        queue = collections.deque()
        res = []
        queue.append(root)
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return res