#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   RebuildBinaryTreeByPreAndMid.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/14 16:47   cecilia      1.0       根据前序遍历和中序遍历重构二叉树
问题描述：
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

'''
思路分析:
前序遍历是【根】【左】【右】
中序遍历是【左】【根】【右】
重建的二叉树的根节点一定是前序遍历的根节点，算法过程如下：
1. 根据前序遍历得到重建树的根节点，设置根节点、左右子树的边界为【pre_root】、【in_left】、【in_right】;
2. 当【in_left】>【in_right】时，子树中序遍历为空，返回null；
3. 遍历中序遍历的的数组，将对应的索引放在哈希表中存储，方便根据前序遍历的到的根节点能够在中序遍历中查找到根节点所在的索引位置；
4. 递归；
   - 根据根结点创建新的树；
   - 根据前序遍历得到的根节点在哈希表中查找中序遍历的根节点索引位置【in_root】;
   - 确定左右子树的边界，继续递归下去；
      对于左子树，根节点是【pre_root+1】,边界为【in_left, in_root - 1】
      对于右子树，根节点是【in_root - in_left + pre_root + 1】, 边界为【in_root + 1, in_right】
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def RebuildBinaryTreeByPreAndMid(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        根据前序遍历和中序遍历重建二叉树
        :param preorder:
        :param inorder:
        :return:
        复杂度分析：时间复杂度O（N），空间复杂度O（N）
        """
        self.hashdict = {}
        self.po = preorder

        for i in range(len(inorder)):
            self.hashdict[inorder[i]] = i  # 哈希表存储中序遍历的每个元素的索引位置

        self.buildTreeByRoot(0, 0, len(inorder) - 1)

    def buildTreeByRoot(self, pre_root: int, in_left: int, in_right: int)-> TreeNode:
        """
        根据根节点，左右字数边界递推
        :param pre_root:根节点索引位置
        :param in_left:左边界
        :param in_right:右边界
        :return:
        """
        # 如果左边界超过右边界，直接返回
        if in_left > in_right:
            return
        # 根据根节点创建树
        root = TreeNode(self.po[pre_root])
        # 获得中序遍历的根节点索引位置
        i = self.hashdict[self.po[pre_root]]
        # 左子树
        root.left = self.buildTreeByRoot(pre_root + 1, in_left, i - 1)
        # 右子树
        root.right = self.buildTreeByRoot(i - in_left + pre_root + 1, i + 1, in_right)
        return root


if __name__ == '__main__':
    s = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    print(s.RebuildBinaryTreeByPreAndMid(preorder, inorder))
