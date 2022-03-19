#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   FindSubString.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/17 15:19   cecilia      1.0        寻找子串
问题描述：给出m个字符串S1，S2，...，Sm和一个单独的字符串T。请在T中选出尽可能多的子串同时满足：
1）这些子串在T中互不相交。
2）这些子串都是S1，S2，...，Sm中的某个串。
问最多能选出多少个子串。

思路分析：先找到所有字串，然后利用寻找最大不相交区间来挑选符合条件的字串
"""
import sys


class Solution:
    def finSubString(self):
        """
        寻找子串
        :param strList:
        :param subStr:
        :return:
        """

        def helper(subList, subStr):
            """
            根据字符串列表，找到所有的子集
            :param subList:
            :param subStr:
            :return:
            """
            res = []
            curr = 0
            while True:
                start = subList.find(subStr, curr)  # 寻找元素i所在的集合代表，该操作用于判断两个元素是否位于同一个集合
                if start != -1:
                    end = start + len(subStr) - 1
                    res.append((start, end))
                    curr = end + 1
                else:
                    break
            return res

        n = int(sys.stdin.readline().strip())
        subList = []
        for i in range(n):
            line = sys.stdin.readline().strip()
            subList.append(line)
        strList = sys.stdin.readline().strip()

        result = []
        for sub in subList:
            tmp = helper(strList, sub)
            if tmp:
                result += tmp

        if result:
            # 排序
            sortedList = sorted(result, key=lambda t: t[1])
            count = 1
            end = sortedList[0][1]
            for i in range(1, len(sortedList)):
                if sortedList[i][0] > end: # 判断两个字符串之间置否存在交集
                    count += 1
                    end = sortedList[i][1]
            print(count)
        else:
            print(0)


if __name__ == '__main__':
    s = Solution()
    s.finSubString()
