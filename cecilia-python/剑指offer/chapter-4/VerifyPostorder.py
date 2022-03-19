#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   VerifyPostorder.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/29 16:42   cecilia      1.0       根据数组验证是否满足某一个二叉树的后序遍历（递归分治或者单调栈）
问题描述：
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int])->bool:
        """
        根据数组判定是否满足某个二叉树的后序遍历
        方法一：递归分治
        :param postorder: 后序遍历数组
        :return:
        复杂度分析：时间复杂度O（N2），每次调用 recur(i,j)减去一个根节点，因此递归占用 O(N) ；最差情况下（即当树退化为链表），每轮递归都需遍历树所有节点，占用 O(N)。
        空间复杂度O（N）；，最差退化为链表
        """
        # 在【i，j】区间中判定是否符合二叉树的后序遍历
        def verifyPostorderByRange(i, j):
            if i >= j: #说明当前的树的节点数目少于1
                return True
            p = i
            while postorder[p] < postorder[j]: p += 1
            m = p
            while postorder[p] > postorder[j]: p += 1
            return (p == j) and verifyPostorderByRange(i, m - 1) and verifyPostorderByRange(m, j - 1)
        return verifyPostorderByRange(0, len(postorder) - 1)




    def verifyPostorderByStack(self, postorder: List[int])->bool:
        """
        根据数组判定是否满足某个二叉树的后序遍历
        方法二：单调栈
        :param postorder: 后序遍历数组
        :return:
        复杂度分析：时间复杂度O（N），遍历 postorder所有节点，各节点均入栈 / 出栈一次，使用 O(N)时间。
        空间复杂度O（N）
        """
        stack = []
        root = float("+inf") # 无穷大
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root:
                return False
            while stack and postorder[i] < stack[-1]: # 如若遍历数组的元素小于当前的栈顶元素，则出栈
                root = stack.pop()
            stack.append(postorder[i]) # 否则加入栈中
        return True
