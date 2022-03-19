#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ArrangementOfStrings.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/8 16:07   cecilia      1.0         字符串的排列(考察回溯递归法)
问题描述：
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,
则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

示例:
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
"""
from typing import List

'''
思路分析：
字符串排列类似集合找同等长度的子集问题，同样的思路仍然采用回溯法解决问题
排列方案数量： 对于一个长度为 n 的字符串（假设字符互不重复），其排列共有 n×(n−1)×(n−2)…×2×1 种方案。

排列方案的生成方法： 根据字符串排列的特点，考虑深度优先搜索所有排列方案。即通过字符交换，先固定第 1 位字符（ n 种情况）、再固定第 2 位字符（ n-1 种情况）、... 、最后固定第 n 位字符（ 1 种情况）。

作者：jyd
链接：https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/mian-shi-ti-38-zi-fu-chuan-de-pai-lie-hui-su-fa-by/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


class Solution:
    def ArrangementOfStrings(self, s):
        """
        字符串排列——》回溯递归
        :param s:
        :return:
        """
        res = []
        sList = list(s)

        def backtrack(x):
            # 终止条件
            if x == len(sList) - 1:
                res.append(''.join(sList))
                return
            # 减枝
            temp_set = set()
            for i in range(x, len(sList)):
                if sList[i] in temp_set:
                    continue
                temp_set.add(sList[i])
                sList[i], sList[x] = sList[x], sList[i]
                # 继续下一个
                backtrack(x + 1)
                sList[i], sList[x] = sList[x], sList[i]

        backtrack(0)
        return res

    def ResverNum(self, nums: List[int], n: int) -> List[int]:
        """
        逆序数组中前n个数字
        :param nums:
        :return:
        """
        L = len(nums)
        if n >= L:
            return nums[::-1]
        if n <= 0:
            return nums
        i, j = 0, n - 1
        res = [x for x in nums[n:]]
        while i < j and j > 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        res.extend([x for x in nums[0:n]])
        return res

    def next_n(n):
        """
        find next n [POJ2453]
        :param n: positive int
        :return next_n
        """
        x = n & -n
        t = n + x
        ans = t | (((n ^ t) // x) >> 2)  # 这里要整除 不然就被转换成float了
        return ans




if __name__ == '__main__':
    # s = input().strip()
    solution = Solution()
    # print(solution.ArrangementOfStrings(s))
    # nums_list = input().strip().split('],[')
    n = int(input().strip())
    # nums = list(map(int, input().strip().split()))
    # print(nums)
    # print(solution.ResverNum(nums, n))
    # 1 2 3 4 5
    print(solution.next_n())

