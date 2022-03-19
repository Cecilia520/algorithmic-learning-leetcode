#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MaxSlidingWindow-I.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/8/7 14:33   cecilia      1.0         滑动窗口最大值
问题描述:
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

提示：

你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
'''
思路分析：
方法一：双指针——但是这种做法在面试中是无法通过的
方法二：维护一个单调的双向队列
即：窗口在每次滑动的过程中，从队列的头部取当前窗口中的最大值，每次窗口新进来一个元素，此刻需要与队列中的元素依次进行大小比较：
    如果刚进来的元素比队列中的尾部元素大，那么先将队列中的尾部元素弹出，然后把刚刚加进来的元素添加至队列的尾部；
    如果刚刚进来的元素比队列中尾部元素小，则加至为队列尾部即可。

** 为什么在元素相等的情况下，也要更新元素呢？**
这是因为窗口是每次向右进行滑动的，每次进入到窗口中的值都有可能是当前窗口中最大的值，我们将相同的值进行更换，其实是为了更新它的索引。这样在窗口进行滑动的时候，每次的最大值都是新的，就能保持最大。
'''
from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        if k == len(nums):
            return [max(nums)]
        start = 0
        end = start + k
        res = []
        while end <= len(nums):
            cur_num = nums[start: end]
            res.append(max(cur_num))
            start += 1
            end += 1
        return res

    def maxSlidingWindowPlus(self, nums: List[int], k: int) -> List[int]:
        """
        单调双向队列（面试推荐做法）
        :param nums:
        :param k:
        :return:
        """
        if not nums or k == 0:
            return []
        queue = collections.deque()
        # 未形成窗口之前
        for i in range(k):
            while queue and queue[-1] < nums[i]:# 如果队列的尾部元素比当前的元素要小，那么出栈
                queue.pop()
            queue.append(nums[i])
        res = [queue[0]]
        # 形成窗口之后
        for i in range(k, len(nums)):
            if queue[0] == nums[i - k]: # 如果队列首元素等于当前的第i-k个元素时，从首部出栈元素
                queue.popleft()
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
            res.append(queue[0])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
    print(s.maxSlidingWindowPlus(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))

