#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   UniqueBinarySearchTrees.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/19 14:17   cecilia      1.0       计算不同的二叉搜索树的种类
问题描述：
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例：
输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


def uniqueBinarySearchTrees(n):
    """
    计算二叉搜索树的种类数
    思路：卡特兰数
       特别的，对于边界情况，当序列长度为 1 （只有根）或为 0 （空树）时，只有一种情况。亦即：G(0)=1,G(1)=1
       假设n个节点存在二叉排序树的个数是G(n)，令f(i)为以i为根的二叉搜索树的个数，则
           G(n) = f(1) + f(2) + f(3) + f(4) + ... + f(n)
       当i为根节点时，其左子树节点个数为i-1个，右子树节点为n-i，则
           f(i) = G(i-1)*G(n-i)f(i)=G(i−1)∗G(n−i)
       综合两个公式可以得到 卡特兰数 公式
           G(n) = G(0)*G(n-1)+G(1)*(n-2)+...+G(n-1)*G(0)
    :param n:
    :return:
    """
    G = [0] * (n + 1)
    G[0], G[1] = 1, 1
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            G[i] += G[j - 1] * G[i - j]  # 卡特兰公式
            print(G[i])

    return G[n]


if __name__ == '__main__':
    print(uniqueBinarySearchTrees(3))
