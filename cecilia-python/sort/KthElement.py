#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   KthElement.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/23 11:06   cecilia      1.0       找到第K个最大的元素
问题描述：Kth Largest Element in an Array (Medium)
例1
Input: [3,2,1,5,6,4] and k = 2
Output: 5
例2
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
"""
import heapq
from typing import List


def findKthLargest1(nums: List[int], k: int) -> int:
    """
    数组中第K个最大的元素
    :param nums:
    :param k:
    :return:
    解题思路一：直接排序，然后返回倒数第 K个元素
    算法分析：时间复杂度为 O(NlogN)，空间复杂度为 O(1)
    """
    return sorted(nums)[-k]


def findKthLargest2(nums: List[int], k: int) -> int:
    """
    数组中第K个最大的元素
    :param nums:
    :param k:
    :return:
    解题思路二：堆排序。
    创建一个大顶堆，将所有数组中的元素加入堆中，并保持堆的大小小于等于 k。这样，堆中就保留了前 k 个最大的元素。
    这样，堆顶的元素就是正确答案。像大小为 k 的堆中添加元素的时间复杂度为 O(logk)，我们将重复该操作 N 次，故总时间复杂度为 O(Nlogk)。
    在 Python 的 heapq 库中有一个 nlargest 方法，具有同样的时间复杂度，能将代码简化到只有一行。
    算法分析：时间复杂度为 O(NlogK)，空间复杂度为 O(k)，用于存储堆
    """
    return heapq.nlargest(k, nums)[-1]


####################小顶堆#######################
# public int findKthLargest(int[] nums, int k) {
#     PriorityQueue<Integer> pq = new PriorityQueue<>(); // 小顶堆
#     for (int val : nums) {
#         pq.add(val);
#         if (pq.size() > k)  // 维护堆的大小为 K
#             pq.poll();
#     }
#     return pq.peek();
# }

def findKthLargest3(nums: List[int], k: int) -> int:
    """
    解题思路三：优先队列——使用一个优先队列存储前k个元素（实质也是堆）
            这种思路和第二种思路一样，只是实现方式不同
    :param nums:
    :param k:
    :return:
    """
    heaq = [float('-inf') for i in range(k)]  # 优先队列
    for i in nums:
        # 始终保持堆顶是最小的元素
        if i > heapq[0]:
            heapq.heappop(heaq)
            heapq.heappush(heaq, i)
    return heaq[0]


def findKthLargest4(nums: List[int], k: int) -> int:
    """
    解题思路四：改进的快排+动态规划的思想
    :param nums:
    :param k:
    :return:
    算法分析：最好的情况下，时间复杂度O(N)，最坏的情况，时间复杂度O(N^2)
    """

    def quicksort(nums, low, high):
        """
        快排
        :param nums:
        :param low:
        :param high:
        :return:
        """
        # 设定区分键
        key = nums[low]
        while low < high:
            # 如果当前的右边的元素超过了区分键，那么
            while low < high and nums[high] >= key:
                high -= 1  # 继续右边索引
            # 如果当前的左边的元素小于区分键，那么继续左移
            while low < high and nums[low] <= key:
                low += 1

            # 如果都不符合，则交换位置
            nums[low], nums[high] = nums[high], nums[low]
        return low

    if nums is None or len(nums) == 0:
        return -1
    L = len(nums)
    low, high = 0, L - 1
    index = quicksort(nums, low, high)

    # 如果当前查找的index不等于总长度-k
    while index != L - k:
        if index < L - k:
            index = quicksort(nums, index + 1, high)
        elif index > L - k:
            index = quicksort(nums, low, index - 1)
    return nums[index]


if __name__ == '__main__':
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(findKthLargest4(nums, k))
