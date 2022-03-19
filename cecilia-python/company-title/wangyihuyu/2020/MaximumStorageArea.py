#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MaximumStorageArea.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/19 21:26   cecilia      1.0       快递盒打包
问题描述：
日常收快递留下一堆快递盒占地方。现在有N个快递盒，盒子不做翻转，每个盒子有自己的长宽高数据，都以整数形式（L，W，H）出现，
将小盒子整理到大盒子里面去（小盒子的长宽高都小于大盒子）。要求快递盒一个套一个（即，打开一个盒子最多只能看到一个小盒子），
最多能整理多少个盒子打包在一起？

示例1：
输入：
[[5,4,3],
[5,4,5],
[6,6,6]]

输出：2
"""
class Solution:
    def maxBoxes(self, boxes):
        """
        :param boxes: int整型二维数组
        :return: int整型
        """
        # 有点类似于区间重叠的问题,可以动态规划求解
        if not boxes or len(boxes) <= 0:
            return 0
        rows = len(boxes)
        cols = len(boxes[0])

        # 先考虑暴力法
        cnt = 0
        for i in range(1, rows):
            for j in range(1, cols):
                if boxes[i][j] <= boxes[i - 1][j - 1]:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    # boxes = input()
    # boxes = int(input("Enter the number of rows in a matrix"))
    # a = [[0 for x in range(n)] for y in range(n)]
    # for i in range(n):
    #     for j in range(n):
    #         a[i][j] = int(input())
    #         print(a[i][j])
    #     print("\n")
    print(s.maxBoxes(boxes=[[5,4,3],[5,4,5],[6,6,6]]))
