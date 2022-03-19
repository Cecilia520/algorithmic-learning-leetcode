#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   kthLargestInBinaryTree.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/8/11 10:09   cecilia      1.0       二叉搜索树的第k大的节点
问题描述：
给定一棵二叉搜索树，请找出其中第k大的节点。

 

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class NodeTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def kthLargestInBinaryTree(self, root: NodeTree, k: int)->int:
        """
        二叉搜索树的第k大节点
        思路：二叉树的中序遍历结果是将数据从小到大排列，然后倒着中序遍历即可得到第k大的节点
        :param root:
        :param k:
        :return:
        时间复杂度：O（N），空间复杂度O（N）,当树退化为链表，为N
        """
        def travel(root: NodeTree):
            if not root: return
            travel(root.right)
            if self.k == 0: return
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            travel(root.left)
        self.k = k
        travel(root)
        return self.res

