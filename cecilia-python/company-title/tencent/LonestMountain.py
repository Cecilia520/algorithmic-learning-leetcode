#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   LonestMountain.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/9/6 20:33   cecilia      1.0         None
"""
from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        left = [1] * n  # 左边有几个连续递增的数
        right = [1] * n  # 右边有几个连续递增的数

        for i in range(1, n):
            if A[i] <= A[i - 1]:
                left[i] = left[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if A[i] <= A[i + 1]:
                right[i] = right[i + 1] + 1

        print("left:{}".format(left))
        print("right:{}".format(right))

        low = [0]*n

        for i in range(len(left)):
            if left[i] > 1:
                for j in range(i+1, len(right)):
                    if right[j] > 1 and A[i] == A[j]:
                        low[i] = left[i] + right[j]

        print("low:{}".format(low))


        # ans = 0
        # for i in range(1, n - 1):
        #     if left[i] > 0 and right[i] > 0:
        #         ans = max(ans, left[i] + right[i] - 1)
        ans = max(low)

        return ans


if __name__ == '__main__':
    s = Solution()
    print("print-1....")
    print(s.longestMountain(A=[5, 4, 3, 2, 1, 2, 3, 4, 5]))
    print("print-2....")
    print(s.longestMountain(A=[87, 70, 17, 12, 14, 86, 61, 51, 12, 90, 69, 89, 4, 65]))
