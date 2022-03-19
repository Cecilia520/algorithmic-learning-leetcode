#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   KLeastNumbers.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/27 17:17   cecilia      1.0       最小的k个数（快排、大根堆）
问题描述：
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
'''
使用堆这个方法可以有两种解题的思路:
思路一: 将全部的数据进行大根堆的排序,然后循环逐一取出前 K 个大的元素,不需要使用额外辅助空间,时间复杂度为O(KlogN)
思路二: 将给定数组前 K 个数据进行大根堆 heap 的排序,然后从第 i = k+1 个元素开始跟大根堆的第一个元素,也就是当前 K 个元素里面的最大值进行比较:
当 arr[i] < heap[0] 时,我们将交换这两个元素,重新进行大根堆的排序,如此进行 n-k 次,我们的堆中就是我们最后要的结果.这个思路的时间复杂度为O(NlogK),空间复杂度为O(K).此方法在海量数据时应用比较好,因为我们的内存有限不能将全部数据读入.

'''
class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 方法一:partition方法(基于快速排序)
        if k > len(arr) or k <= 0:
            return []
        start = 0
        end = len(arr) - 1
        index = self.quickSort(arr, start, end)
        while index != k-1:
            print(index)
            if index > k-1:
                end = index - 1
                index = self.quickSort(arr, start, end)
            if index < k-1:
                start = index + 1
                index = self.quickSort(arr, start, end)
        return arr[:k]

    def quickSort(self, arr, start, end):
        low = start
        high = end
        temp = arr[start]
        while low < high:
            while low < high and arr[high] >= temp:
                high -= 1
            arr[low] = arr[high]
            while low <high and arr[low] < temp:
                low += 1
            arr[high] = arr[low]
        arr[low] = temp
        return low

    def getLeastNumbersByBigHeap(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k <= 0 or k > len(arr):
            return []
        heap = self.build_heap(arr[:k])
        print(heap)
        for i in range(k, len(arr)):
            if arr[i] < heap[0]:
                heap[0] = arr[i]
                self.sink(heap, 0)
        return heap

    def sink(self, array, k):
        n = len(array)
        left = 2 * k + 1
        right = 2 * k + 2
        if left >= n: return
        max_i = left
        if right < n and array[left] < array[right]:
            max_i = right
        if array[max_i] > array[k]:
            array[max_i], array[k] = array[k], array[max_i]
            self.sink(array, max_i)

    def build_heap(self, list_):
        n = len(list_)
        for i in range(n // 2, -1, -1):
            self.sink(list_, i)
        return list_
