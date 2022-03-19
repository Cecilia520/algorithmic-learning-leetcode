#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PrintBinaryTree-I.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/29 17:53   cecilia      1.0       从上到下交替打印二叉树（之字形）
问题描述：
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

 

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
  [20,9],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
import collections

'''
思路分析：
    根据第二种的题型，第一层是从左到右遍历，第二层是从右到左遍历，，由此可以在第二种题型基础上，奇数可以从左到右遍历，第二层是从右到左遍历
    由于双端队列可以在队首队尾同时添加元素，可以使用一个暂时的双端队列进行维护添加元素的列表
'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def printBinaryTree(self, root: TreeNode)->List[List[int]]:
        """
        层次交替打印二叉树
        :param root:
        :return:
        复杂度分析：时间复杂度O（N），空间复杂度O（N）
        """
        if not root:
            return []
        queue = collections.deque([root])
        res = []
        while queue:
            tmp = collections.deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if len(res) % 2 == 0: #偶数加在队列头部
                    tmp.append(node.val)
                else:
                    tmp.appendleft(node.val) #奇数加在队列尾部
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(list(tmp))
        return res
