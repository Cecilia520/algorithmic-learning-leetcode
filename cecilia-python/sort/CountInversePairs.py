#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   CountInversePairs.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/17 18:24   cecilia      1.0        统计数组的逆序对个数
问题描述：
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007

提示：
暴力法时间复杂度是O(N^2)
优化思路：归并排序的改进（NlogN）
"""


class Solution:
    def __init__(self):
        self.count = 0

    def InversePairs(self, data):
        """
        数据的逆序对的个数统计
        :param data:
        :return:
        """
        def MergeSort(lists):
            """
            归并排序
            :param lists:
            :return:
            """
            if len(lists) <= 1:
                return lists

            # 根据中间的数进行拆分成两个小数组，分别进行归并排序
            num = int(len(lists) / 2)
            left = MergeSort(lists[:num])
            right = MergeSort(lists[num:])

            r, l = 0, 0
            result = []

            # 小数组内部进行排序
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
                    self.count += len(left) - l
            result += right[r:]
            result += left[l:]
            return result

        # 合并
        MergeSort(data)
        return self.count % 1000000007


if __name__ == '__main__':
    s = Solution()
    print(s.InversePairs(data=[1, 2, 3, 4, 5, 6, 7, 0]))
