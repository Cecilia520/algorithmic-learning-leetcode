#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PrintBinaryTree-I.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/29 17:53   cecilia      1.0       从上到下层级打印二叉树
问题描述：
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

'''
思路分析：
在第一道题的基础上，这道题要求是层序遍历，每一层遍历的数据都存在一个list中，最后返回所有层的list
同样的可以采取队列的解决问题
'''
import collections


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def printBinaryTree(self, root: TreeNode) -> List[List[int]]:
        """
        从上到下层序遍历打印二叉树
        :param root:
        :return:
        """
        if not root:
            return []
        queue = collections.deque()
        res = []
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp)
        return res
