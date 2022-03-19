#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MaxSlidingWindow-I.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/5 20:04   cecilia      1.0        滑动窗口的最大值
问题描述：
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。

进阶：

你能在线性时间复杂度内解决此题吗？


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

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def maxSlidingWindow(nums, k):
    """
    滑动窗口最大值
    双指针法
    :param nums:
    :param k:
    :return:
    时间复杂度O(nK),空间复杂度O(1)
    """
    if not nums or len(nums) <= 0:
        return []
    if k > len(nums):
        return []
    start = 0
    res = []
    for end in range(k - 1, len(nums)):
        res.append(max(nums[start:end + 1]))
        start += 1
    return res


def maxSliadWindowPlus(nums, k):
    """
    动态规划求解或者双向队列
    算法的思想是:将输入数组分割成有 k 个元素的块。若 n % k != 0，则最后一块的元素个数可能更少。
    状态转移：从左到右求解max，从右到左求解max
    :param nums:
    :param k:
    :return:
    时间复杂度O(n),空间复杂度O(n)
    """
    if not nums or len(nums) <= 0:
        return []
    if k > len(nums):
        return []

    n = len(nums)

    # 定义状态，分别存储从左到右max的数组以及从右到左的max数组
    left = [0] * n
    right = [0] * n

    # 初始化
    left[0] = nums[0]
    right[n - 1] = nums[n - 1]

    # 状态转移过程
    for i in range(1, n):
        # from left to right
        if i % k == 0:  # 说明刚好满了一个窗口
            left[i] = nums[i]
        else:
            left[i] = max(left[i - 1], nums[i])  # 不满足一个窗口的时候，说明在窗口内部比较找最大值

        # from right to left
        j = n - i - 1
        if (j + 1) % k == 0:
            right[j] = nums[j]
        else:
            right[j] = max(right[j + 1], nums[j])

    res = []
    # 总共有n-k+1个窗口
    for i in range(n - k + 1):
        res.append(max(right[i], left[i + k - 1]))

    return res


if __name__ == '__main__':
    print(maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
    print(maxSliadWindowPlus(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
