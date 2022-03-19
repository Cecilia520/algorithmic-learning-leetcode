#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   GetMinOperatorDNA.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/24 22:12   cecilia      1.0       统计最小操作DNA的次数
问题描述：有一种特殊的DNA，仅仅由核酸A和T组成，长度都为n，科学家有一种新的手段，可以改变这种DNA，
每一次可以交换两个核酸的位置，也可以将某个特定位置的核酸进行修改。现在有一个DNA，科学家希望将其改造成另一种DNA，求取最少的操作次数
输入：原始DNA D1=“ATTTAA”，目标DNA D2=“TTAATT”
输出：3
解释：
将原始DNA第一个位置的核酸的A修改为T；
将原始DNA的3和5位置的核酸进行交换；
将原始DNA的4和6位置的核酸进行交换。


思路分析：动态规划
根据题目意思进行简化后，大致的意思就是可以修改或者交换某个特定位置的核酸的手段将其改造成另一种核酸的最少次数。
首先比较明确的是修改一次，加1，交换一次，加1，那么操作的所有集合累计成一个所要求的解集合，如果每个小集合都是最优的，那么累计后的大集合也是最优的。
1.确定转移状态：修改或者交换。代表交换：dp[i-1][j-1]；修改DNA：dp[i][j-1]
2.初始化。
3.状态转移过程。
"""
def getMinOperators(D1: str, D2: str) -> int:
    n, m = len(D1), len(D2)

    # 判断边界情况
    if n <= 0 or m <= 0:
        return 0

    # 定义状态转移数组
    dp = [[0 for _ in range(n)] for _ in range(m)]

    # 初始化
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + 1
    for i in range(1, m):
        dp[0][i] = dp[0][i - 1] + 1

    for i in range(1, n):
        for j in range(1, m):
            if D1[i - 1] == D2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1]) + 1

    return dp[n - 1][m - 1]

if __name__ == '__main__':
    print(getMinOperators(D1="ATTTAA", D2="TTAATT"))
    # print(getMinOperators(D1="ATATTA", D2="TTAATT"))