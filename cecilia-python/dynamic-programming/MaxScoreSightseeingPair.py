#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MaxScoreSightseeingPair.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/30 12:00   cecilia      1.0       最佳观光组合
问题描述：
给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。
一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。
返回一对观光景点能取得的最高分。

示例：

输入：[8,1,5,2,6]
输出：11
解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-sightseeing-pair
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


def maxScoreSightseeingPairDoublePointer(A: List[int]) -> int:
    """
    双指针法
    :param A:
    :return:
    算法分析：时间复杂度O(n^2),空间复杂度O(1),但是当数组长度趋近于无穷大，那么时间复杂度会特别大，不适合。
    """
    if not A:
        return 0

    maxScore = A[0] + A[1] - 1

    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            current = A[i] + A[j] + i - j
            maxScore = max(current, maxScore)
    return maxScore


def maxScoreSightseeingPair(A: List[int]) -> int:
    """
    计算最佳观光组合
    思路分析：根据i<j的特性，发现动态规划表实际上是遍历斜对角，和三角形求解最小路径和类似.
        在这道题中，根据题友的提供，可以将A[i]+A[j]+i-j进行分解成A[i]+i和A[j]-j，最优子结构问题转化成A[i]+i最大时，那么最后的值就是最大值。
    :param A: 旅游景点数组
    :return:
    算法分析：时间复杂度O(n),空间复杂度O(1)
    """
    if not A:
        return 0

    n = len(A)

    # 此处可以不需要使用额外的空间进行存储，直接使用两个变量分别存储A[i]+i的值和最终的最大和
    max_sum = 0
    left_sum = 0

    for i in range(n):
        # 此处与双指针的区别在于，每次迭代时，都将最大的leftSum的值进行存储起来，下次迭代不需要再计算，减少了时间复杂度
        max_sum = max(max_sum, left_sum + A[i] - i)
        left_sum = max(left_sum, A[i] + i)

    return max_sum


if __name__ == '__main__':
    print(maxScoreSightseeingPair(A=[8, 1, 5, 2, 6]))
