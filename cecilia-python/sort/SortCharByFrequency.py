#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   SortCharByFrequency.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/2 14:16   cecilia      1.0        给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
题目描述：给字符串中的字符按照出现的频率降序排序
示例1：
输入:"tree"
输出:"eert"
解释:
'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。

示例2：
输入:"cccaaa"
输出:"cccaaa"
解释:
'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
注意"cacaca"是不正确的，因为相同的字母必须放在一起。

示例3：
输入:"Aabb"
输出:"bbAa"
解释:
此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
注意'A'和'a'被认为是两种不同的字符。

"""
import collections


def sortCharByFrequency(s: str) -> str:
    """
    将字符串中的字符按照出现频率的降序排序
    思路分析：首先将字符串中的字符存储在数组中，并统计每个字符出现的频率，以字典形式进行存储，然后对此进行降序排列，最后组合成新的字符串输出
    解决方案一：常规排序
    算法分析：时间复杂度：O(nlogn), 空间复杂度O(n)
    :param s:
    :return:
    """
    strdict = dict(collections.Counter(s))
    res = sorted(strdict.items(), key=lambda x: x[1], reverse=True)
    print(res)
    answer = ''
    for (key, value) in res:
        if value == 1:
            answer.append(key)
        elif value > 1:
            for i in range(value):
                answer.append(key)
    return "".join([str(x) for x in answer])


def sortCharByFrequency1(s: str) -> str:
    """
    解决方案二：根据第一种解题思路，从代码的基本层面上进行优化
    算法分析：从时间计算来看，时间减少，并且内存也减少。时间复杂度O(KlogK),空间复杂度O(K)
    :param s:
    :return:
    """
    set1 = set(s)
    strdict = {x: s.count(x) for x in set1}
    res = sorted(strdict, key=lambda k: strdict[k], reverse=True)
    answer = ""
    for i in res:
        answer += strdict[i] * i  # 字符串的加法
    return answer


def sortCharByFrequency2(s: str) -> str:
    """
    将字符串中的字符按照出现频率的降序排序
    思路分析：首先将字符串中的字符存储在数组中，并统计每个字符出现的频率，以字典形式进行存储，然后对此进行降序排列，最后组合成新的字符串输出
    解决方案三：排序处进行优化，采用桶排序优化排序
    算法分析：实验显示，计算时间变长了，并且计算内存由于桶的存储而浪费了一些内存，这种方式不可取！
    :param s:
    :return:
    """
    sortstr = dict(collections.Counter(s))
    # 根据字符串长度创建桶
    bucketList = [[] for i in range(len(list(s)) + 1)]
    for (key, value) in sortstr.items():
        bucketList[value].append(key)
    print(bucketList)
    answerlist = []
    answer = ""
    strlenth = len(s)
    for k in range(strlenth, 0, -1):
        if bucketList[k]:
            if len(bucketList[k]) > 1:
                for j in range(len(bucketList[k])):
                    answerlist.extend(bucketList[k][j] * k)
            else:
                answerlist.extend(bucketList[k] * k)
    for char in answerlist:
        answer += char
    return answer


if __name__ == '__main__':
    s = "cccaaa"
    print(sortCharByFrequency2(s))
