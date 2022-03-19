#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   UniqueBinarySearchTreesII.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/17 17:07   cecilia      1.0       构建不同的二叉搜索树
问题描述：
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例：
输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        """
        定义一个二叉树
        """
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def uniqueBinarySearchTreesII(self, n) -> List[TreeNode]:
        """
        构建多个二叉搜索树
        思路分析：第一道题目是只需要输出总的种类数即可，但是在这道题目中，需要直接输出所有树的集合
        总体思路：分别构建左子树和右子树，再以根节点将左右子树进行连接起来即可，其核心思维也是动态规划的思维。将整个问题分解成左右子树，最后进行合并。
        1. 遍历数组，以i为根节点，分别递归计算左子树和右子树；
        2. 分别遍历左右子树，以根节点i进行连接，并加入集合中；
        3. 如果n不存在或者为0，返回空集合，否则返回集合
        :param n:
        :return:
        算法分析：时间复杂度O(4^n/n^(1/2)),空间复杂度O(4^n/n^(1/2))
        """

        def generateTrees(start, end):
            """
            构建一个二叉搜索树
            :param start:开始节点
            :param end:结尾节点
            :return:
            """
            if start > end:
                return [None, ]

            allTrees = []
            # 选作i作为根节点
            for i in range(start, end + 1):
                # 左子树的节点
                leftNodes = generateTrees(start, i - 1)
                # 右子树节点
                rightNodes = generateTrees(i + 1, end)

                # 将左右子树根据root连接起来
                for l in leftNodes:
                    for r in rightNodes:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        allTrees.append(current_tree)
            return allTrees

        return generateTrees(1, n) if n else []

if __name__ == '__main__':
    solution = Solution()
    print(solution.uniqueBinarySearchTreesII(3))
