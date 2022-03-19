#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PathSum-III.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/10 21:11   cecilia      1.0       统计一个树的路径和是否等于一个指定的数的路径条数
问题描述：
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
def pathSumII(root: TreeNode, sum):
    """
    统计一个树的路径和是否等于一个指定的数的路径条数
    思路分析：
    :param root:
    :param sum:
    :return:
    """
    def pathSumWithRoot(root, sum):
        """
        统计在根节点的情形的路径和的路径种数
        :param root:
        :param sum:
        :return:
        """
        count = 0
        if root is None:
            return False
        if root and root.val == sum:
            count += 1

        # 统计左右子树节点和为sum的count
        count += pathSumWithRoot(root.letf, sum - root.val) + pathSumWithRoot(root.right, sum - root.val)
        return count

    if root is None:
        return 0
    count = 0
    count += pathSumWithRoot(root, sum) + pathSumII(root.left, sum) + pathSumII(root.right, sum)
    return count