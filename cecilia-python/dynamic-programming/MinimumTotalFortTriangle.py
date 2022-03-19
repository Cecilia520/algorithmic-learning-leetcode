#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MinimumTotalFortTriangle.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/29 21:06   cecilia      1.0        三角形最小路径和
问题描述：
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：
会考察如何压缩内存空间！
如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


def minimumTotalFortTriangle(triangle: List[List[int]]) -> int:
    """
    求解三角形最小路径和
    思路分析：
    动态规划分析：
    首先题目的原型就是求解连续子序列的最大和，同样的和机器人走网格的题型也很类似，只是这里变成了三角形。
    其次最关键的是分析动态转移的规律，累计是先从第一行的第一个元素往下以及相邻元素进行累加和，两个和之间会有比较，选取最小和，到了第三行，同理进行选取最小和，直到最后结束。
    由此可以知道，dp[i][j]代表第i行第j列的累加和，是由上一层的第i-1行第j列以及第i-1行第j-1列求min得到的结果，那么状态转移方程为：
        dp[i][j] = min(dp[i-1][j], dp[i-1][j-1])+triangle[i][j]
    另外还需要分析边界的初始化值：
        dp[0][0] = triangle[0][0]
        dp[1][0] = triangle[0][0] + triangle[1][0]
        dp[0][1] = triangle[0][0] + triangle[0][1]
        也就是可以看出，第一列的所有值是直接从上一行而来，最右边的值是从左上角而来，由此得出：
        dp[i][j] = dp[i-1][j] + triangle[i-1][j]
        dp[i][j] = dp[i-1][j-1] + triangle[i-1][j-1]
    :param triangle:
    :return:
    算法分析：时间复杂度O(mn),空间复杂度O(nm),此时额外的空间可以考虑再次优化。
    """
    if not triangle:
        return 0

    if len(triangle) == 1:
        return triangle[0][0]

    m = len(triangle)
    print(m)

    # 定义状态转移状态
    dp = [[0 for _ in range(m)] for _ in range(m)]
    print(dp)
    # dp = triangle

    # 初始化
    dp[0][0] = triangle[0][0]
    dp[1][0] = dp[0][0] + triangle[1][0]
    dp[1][1] = dp[0][0] + triangle[1][1]

    for i in range(2, m):
        for j in range(i+1):
            if j == 0: #左边角的元素
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1: # 右边角的元素
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

    # 计算最后一列得出所有可能性的结果，需要找出最小的和
    minValue = dp[-1][0]
    for i in range(len(dp)):
        minValue = min(minValue, dp[-1][i])
    return minValue

def minimumTotalFortTrianglePlus(triangle: List[List[int]]) -> int:
    """
    动态规划优化版：
        以上普通的思维是利用二维数组进行存储，空间复杂度是O(n^2)左右，此处可以将思维进行转换，自底向上进行遍历，将最后一行的大小作为动态转移状态数组的大小。
        思路也就是从倒数第二行进行向上遍历，最后得到的最优化的值就是dp[0],或者直接使用已经提供的三角形的数组
    :param triangle:
    :return:
    算法分析：时间复杂度O(n^2),空间复杂度O(n)或者O(1)
    """
    if not triangle:
        return 0

    if len(triangle) == 1:
        return triangle[0][0]

    # 定义状态，直接使用最后一行
    dp = triangle[-1]

    # 从倒数第二行进行往上遍历
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
            print(dp)
    return dp[0]



if __name__ == '__main__':
    print(minimumTotalFortTriangle(triangle=[[2],
                                           [3, 4],
                                         [6, 5, 7],
                                        [4, 1, 8, 3]]))
