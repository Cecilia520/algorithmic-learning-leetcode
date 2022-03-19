#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   IsSubTreeStructure.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/24 15:07   cecilia      1.0       是否是树的子结构
问题描述：
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：

输入：A = [3,4,5,1,2], B = [4,1]
输出：true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
'''
思路分析：
很多有关树的题目的都可以使用递归实现，判断是否是某棵树的子结构，一般思路就是先判断该子树是否是根节点的树；
如果不是，接着递归到左子树或者右子树，依次判断
'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isSubTreeStructure(self, A: TreeNode, B: TreeNode) -> bool:
        """
        判断B是否是A的子树
        :param A:
        :param B:
        :return:
        复杂度分析：时间复杂度O（MN），其中M，N分别代表A和B树的结点的数量，遍历A耗费O（M），isSubTreeStructureByRoot（N），总的就是O（MN）
        空间复杂度O（M），最糟糕的情况是两棵树都退化为链表
        """
        def isSubTreeStructureByRoot(A, B):
            if not B:
                return True
            if not A or A.val != B.val:
                return False
            return isSubTreeStructureByRoot(A.left, B.left) and isSubTreeStructureByRoot(A.right, B.right)
        return bool(A and B) and isSubTreeStructureByRoot(A, B) or self.isSubTreeStructure(A.left, B) or self.isSubTreeStructure(A.right, B)
