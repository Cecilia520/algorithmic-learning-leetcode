#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   28.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/18 10:27   cecilia      1.0         None
题目描述：
我们称一个长度为n的序列为正则序列，当且仅当该序列是一个由1~n组成的排列，即该序列由n个正整数组成，取值在[1,n]范围，且不存在重复的数，同时正则序列不要求排序。

有一天小团得到了一个长度为n的任意序列，他需要在有限次操作内，将这个序列变成一个正则序列，每次操作他可以任选序列中的一个数字，并将该数字加一或者减一。

请问他最少用多少次操作可以把这个序列变成正则序列？



输入描述
输入第一行仅包含一个正整数n，表示任意序列的长度。(1<=n<=20000)

输入第二行包含n个整数，空格隔开，表示给出的序列，每个数的绝对值都小于10000。

输出描述
输出仅包含一个整数，表示最少的操作数量。

样例输入
5
-1 2 3 10 100
样例输出
103
"""
class Solution:
    def to_regex_seq(self, n, nums):
        """
        正则序列
        :param nums:
        :return:
        """
        if n == 0:
            return 0
        nums = sorted(nums)
        steps = 0
        for i in range(n):
            steps += abs((i+1) - nums[i])
        return steps

if __name__ == '__main__':
    s = Solution()
    n = int(input())
    nums = list(map(int, input().strip().split()))
    print(s.to_regex_seq(n, nums))

