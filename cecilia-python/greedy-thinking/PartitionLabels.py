#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   PartitionLabels.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/8 15:14   cecilia      1.0        分隔字符串使同种字符出现在一起
问题描述：
字符串S由小写字母组成，要求尽可能地将该字符串进行切分多个片段，同一个字母只会出现在其中一个片段。
返回一个表示每个字符串片段的长度的列表。

示例1：
输入: S = "ababcbacadefegdehijhklij"
输出: [9,7,8]
解释:
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。

注意:
    S的长度在[1, 500]之间。
    S只包含小写字母'a'到'z'。
"""


def partitionLabel(S) -> []:
    """
    分割字符串使得同种字母出现在一起
    思路分析：
        可以采用贪心思想来求解问题。——
        1.首先遍历字符串将其转变成字典形式，存储每个字符最后一次出现的位置；
        2.遍历字符串中的每个字符，记录当前字符的最大index；
        3.判断索引的最大index是否和字典中已经存储的相等，相等，则加入list中，开始i+1查找下一个区间。
    :param S: 字符串
    :return:
    算法分析：时间复杂度O(N),空间复杂度O(N)
    """
    lastcharindex = {c: i for i, c in enumerate(S)}
    # print(lastcharindex)

    start = 0 #区间开始index
    end = 0 # 区间终止index
    answer = []
    ans = []

    for i, c in enumerate(S):
        end = max(end, lastcharindex[c])
        if end == i:
            answer.append(i - start + 1)
            ans.append(S[start:end])
            start = i + 1
    return answer, ans


if __name__ == '__main__':
    S = "ababcbacadefegdehijhklij"
    print(partitionLabel(S))
