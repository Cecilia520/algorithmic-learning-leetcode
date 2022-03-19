#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   32.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/28 15:44   cecilia      1.0         None
"""
"""
该题可以采取动态规划的思路进行解决，主要重点在于动态数组的定义和状态转移过程。在此处，
设定dp【i】数组表示元素i能够使得完全平方数的个数最少。
"""
import math


class Solution:
    def get_num_squares(self, n):
        """
        完全平方数
        :@param n
        """
        a = [i ** 2 for i in range(0, int(math.sqrt(n) + 1))]
        dp = [100000] * (n+1)

        dp[0] = 0

        for i in range(1, n + 1):
            for j in a:
                if i < j:
                    break
                dp[i] = min(dp[i], dp[i - j] + 1)
        return dp[-1]
        # while n % 4 == 0:
        #     n /= 4
        # if n % 8 == 7:
        #     return 4
        # tmp = 0
        # while tmp ** 2 <= n:
        #     index = int((n - tmp ** 2)**0.5)
        #     if tmp ** 2 + index ** 2 == n:
        #         return (not not tmp) + (not not index)
        #     tmp += 1
        # return 3
    # def is_square(self, n:int)->bool:
    #     """
    #     判断是否是
    #     :param n:
    #     :return:
    #     """
    #     square = int(math.sqrt(n))
    #     return square*square == n


        # a = [i ** 2 for i in range(0, int(math.sqrt(n) + 1))]
        # dp = [float('inf')] * (n + 1)
        #
        # dp[0] = 0
        #
        # for i in range(1, n + 1):
        #     for j in a:
        #         if i < j:
        #             break
        #         dp[i] = min(dp[i], dp[i - j] + 1)
        # return dp[-1]

        # while (n & 3) == 0:
        #     n >>= 2
        # if (n & 7) == 7:
        #     return 4
        # if self.is_square(n):
        #     return 1
        # for i in range(1, int(n**0.5)+1):
        #     if self.is_square(n-i*i):
        #         return 2
        # return 3




if __name__ == '__main__':
    n = int(input().strip())
    solution = Solution()
    print(solution.get_num_squares(n))