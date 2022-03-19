#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   KSumForContinuousSequence.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/9 10:23   cecilia      1.0         和为target的连续正整数序列
问题描述：
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
"""
from typing import List

'''
对于和为target的连续正整数序列，最开始的暴力想法就是以每个正整数为起点进行搜索是否存在序列和为target的序列，且长度大于2；
但是，我们可以使用另一种方法，双指针的方法，设定起始位置和终止位置[start, end]来作为序列区间,sum=(start+end)*(end-start+1)/2,start=1,end=2;

如果 sum<target 则说明指针 r 还可以向右拓展使得 sum 增大，此时指针 r 向右移动，即 r+=1
如果 sum>target 则说明以 l 为起点不存在一个 r 使得 sum=target ，此时要枚举下一个起点，指针 l 向右移动，即l+=1
如果 sum==target 则说明我们找到了以 l 为起点得合法解 [l,r] ，我们需要将 [l,r]的序列放进答案数组，且我们知道以 l 为起点的合法解最多只有一个，所以需要枚举下一个起点，指针 l 向右移动，即 l+=1

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/mian-shi-ti-57-ii-he-wei-sde-lian-xu-zheng-shu-x-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


class Solution:
    def KSumForContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        l = 1  # 起点
        r = 2  # 动态变化窗口大小[l,r]
        while l < r:
            tmp_sum = (l + r) * (r - l + 1) / 2  # 计算连续正整数的和，（首项+尾项）*项数 / 2
            cur_sum = []
            if tmp_sum == target:
                # 遍历每个元素，将其存储到数组中
                for i in range(l, r + 1):
                    cur_sum.append(i)
                res.append(cur_sum)
                l += 1
            elif tmp_sum > target:  # 如果当前的和比目标的要大，说明不存在这样的区间【l,r】，需要继续遍历下一个起点l
                l += 1
            else:
                # 如果当前的和小于目标的值，说明当前的区间太小了，需要继续增大r
                r += 1
        return res


if __name__ == '__main__':
    s = Solution()
    target = int(input().strip())
    print(s.KSumForContinuousSequence(target=target))
