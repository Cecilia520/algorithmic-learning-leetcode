#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PrintMatrixBySpiralOrder.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/8/21 18:01   cecilia      1.0       顺时针打印矩阵
问题描述：
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

'''
思路分析：
    可以按照层数来打印，对于每层，从左上方开始以顺时针的顺序遍历所有元素。
    假设当前层的左上角位于 (top,left)，右下角位于 (bottom,right)，按照如下顺序遍历当前层的元素——

    1.从左到右遍历上侧元素，依次为 (top,left) 到 (top,right)。

    2.从上到下遍历右侧元素，依次为 (top+1,right) 到 (bottom,right)。

    3.如果 left<right 且 top<bottom，则从右到左遍历下侧元素，依次为 (bottom,right−1) 到 (bottom,left+1)，以及从下到上遍历左侧元素，依次为 (bottom,left) 到 (top+1,left)。
    遍历完当前层的元素之后，将 left 和 top 分别增加 11，将 right 和 bottom 分别减少 11，进入下一层继续遍历，直到遍历完所有元素为止。
'''


class Solution:
    def PrintMatrixBySpiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        顺时针打印矩阵
        :param matrix:
        :return:
        复杂度分析：时间复杂度O（mn），空间复杂度O（1）
        """
        if not matrix or not matrix[0]:
            return []

        rows, columns = len(matrix), len(matrix[0])
        order = []
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1): # 从左到右
                order.append(matrix[top][column])
            for row in range(top + 1, bottom + 1): # 从上到下
                order.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right-1, left, -1):
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return order


if __name__ == '__main__':
    s = Solution()
    print(s.PrintMatrixBySpiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
