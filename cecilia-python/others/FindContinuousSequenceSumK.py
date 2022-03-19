#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   FindContinuousSequenceSumK.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/18 17:19   cecilia      1.0       和为K的所有连续子序列
问题描述：
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列?

思路分析：
链接：https://www.nowcoder.com/questionTerminal/c451a3fd84b64cb19485dad758a55ebe
来源：牛客网

1）由于我们要找的是和为S的连续正数序列，因此这个序列是个公差为1的等差数列，而这个序列的中间值代表了平均值的大小。假设序列长度为n，那么这个序列的中间值可以通过（S / n）得到，知道序列的中间值和长度，也就不难求出这段序列了。
2）满足条件的n分两种情况：
n为奇数时，序列中间的数正好是序列的平均值，所以条件为：(n & 1) == 1 && sum % n == 0；
n为偶数时，序列中间两个数的平均值是序列的平均值，而这个平均值的小数部分为0.5，所以条件为：(sum % n) * 2 == n.
3）由题可知n >= 2，那么n的最大值是多少呢？我们完全可以将n从2到S全部遍历一次，但是大部分遍历是不必要的。为了让n尽可能大，我们让序列从1开始，
根据等差数列的求和公式：S = (1 + n) * n / 2，得到.
"""


def findContinuousSequence(tsum):
    # write code here
    if tsum < 3:  # 要求长度大于2
        return []
    # 使用双指针构建窗口滑动
    low = 1
    high = 2
    res = []
    while low < high:
        # 窗口内部的数据可以看作是等差为1，首项是low，尾项是high的等差序列，可以求和
        windowsSum = int((low + high) * (high - low + 1) / 2)
        if windowsSum == tsum:
            # 如果总和为sum，那么将窗口中的数据纷纷加入list中
            res.append([x for x in range(low, high + 1, 1)])
            # 继续左移
            low += 1
        elif windowsSum < tsum:
            high += 1
        else:
            low += 1
    return res


def findContinuousSequence1(tsum, L):
    """
    优化思路一：直接减少循环次数，每次折半查找
    :param tsum:
    :return:
    """
    if tsum < 0:
        return []
    res = []

    for i in range(L, int(tsum / 2 + 1)):
        for j in range(i, int(tsum / 2 + 2)):
            currSum = int((i + j) * (j - i + 1) / 2)
            if currSum > tsum:
                break
            elif currSum == tsum:
                tmpList = [x for x in range(i, j + 1)]
                res.append(tmpList)
    return res[-1]


def findContinuousSequence2(N, L):

    for i in range(L, 101):
        if (N - i * (i - 1) / 2) % i == 0:
            start = int((N - i * (i - 1) / 2) // i)
            end = int((N - i * (i - 1) / 2) // i + i - 1)
            for j in range(start, end):
                print(str(j) + ' ')
        else:
            print(int((N - i * (i - 1) / 2) // i + i - 1))
    print("No")


if __name__ == '__main__':
    print(findContinuousSequence1(100, 6))
