#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   20.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/9/26 20:30   cecilia      1.0         None
第一行四个数n,m,s,t。

接下来m行，每行三个数u,v,w，表示u和v之间有一条边权为w的无向边。

输入保证s点和t点连通。

1≤n≤100,000；0≤m≤200,000；1≤w≤1,000,000,000

5 6 1 5
1 5 100
1 2 10
2 5 5
1 3 3
3 4 2
4 5 1

输入样例2：
3 3 1 3
1 2 99
2 3 99
1 3 100
输出样例2：
99
样例解释：
对于样例，简单来看乌龟有1-5，1-2-5，1-3-4-5三个方案可以选择。三个方案中最大权值分别为100，10，3，所以最终乌龟选择了第三条路1-3-4-5。
"""


class Solution:
    def getMinNums(self, a: int, b, k, v)->int:
        """
        计算最少箱子的个数
        :param a:物体数
        :param b:隔板数
        :param k:隔间数
        :param v:隔间放的物体
        :return:
        """
        res = 0
        while b > k - 1 and a > 0:
            a = a - k * v
            b = b - k + 1
            res += 1
        if a > 0:
            if b > 0:
                a = a - (b+1)*v
                res += 1
        while a > 0:
            a -= v
            res += 1
        return res
# class Solution:
#     def getMinNums2(self, a: int, b, k, v)->int:
#         """
#         计算最少箱子的个数
#         :param a:物体数
#         :param b:隔板数
#         :param k:隔间数
#         :param v:隔间放的物体
#         :return:
#         """
#         remain_a = a
#         remain_b = b
#         res = 0
#         while remain_a > 0:
#             if k > 1 and remain_b >= k - 1:
#                 remain_b = remain_b - (k - 1)
#                 remain_a = remain_a - k * v
#                 res += 1
#             else:
#                 remain_a = remain_a - 1
#                 res += 1
#         return res

if __name__ == '__main__':
    s = Solution()
    while True:
        try:
            a, b, k, v = map(int, input().strip().split())
            print(s.getMinNums(a, b, k, v))
        except Exception as e:
            break
