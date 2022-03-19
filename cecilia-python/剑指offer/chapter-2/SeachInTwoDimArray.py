#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   SeachInTwoDimArray.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/9 10:14   cecilia      1.0         二维数组中的查找
问题描述：
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数。

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
'''
思路分析：
第一，常规思路就是遍历矩阵，分别从左到右、从上到下依次遍历，这种方法的时间复杂度是O(N*M),时间复杂度过高；
第二，线性查找，可以从矩阵的右上角出发遍历，选择右上角的目的是因为在当前数据是一行中最大的，一列中最小的，当数据和目标值不一样的时候，可以有规律地变化；
如果当前的数据等于目标值，那么返回true；
如果当前的数据大于目标值，row--；
如果当前的数据小于目标值，column++。
'''


class Solution:
    def SeachInTwoDimArray(self, matrix, target):
        """
        查找目标数据
        :param matrix:
        :param target:
        :return:
        复杂度分析：时间复杂度O(M+N),空间复杂度O(1)
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        columns = len(matrix[0])
        i, j = 0, columns - 1
        while i < len(matrix) and j >= 0:
            cur_num = matrix[i][j]
            print(cur_num)
            if cur_num == target:
                return True
            elif cur_num > target:  # 说明当前的数据比目标值要大，j--
                j -= 1
            else:  # 说明当前的数据比目标值要小，i++
                i += 1
        return False


if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target = 5
    print(s.SeachInTwoDimArray(matrix=matrix, target=target))
