#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   33.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/28 16:04   cecilia      1.0         None
"""
class Solution:
    def getLengthOfLongestSubString(self, s:str)->int:
        """
        获得最长无重复子串长度
        :param s:
        :return:
        """
        n = len(s)
        res = 0
        end = -1
        hash_dict = {}
        for k, v in enumerate(s):
            if v in hash_dict:
                end = max(end, hash_dict[v])
            res = max(res, k - end)
            hash_dict[v] = k
        return res
if __name__ == '__main__':
    while True:
        try:
            line = input().strip()
            solution = Solution()
            if line != '':
                print(solution.getLengthOfLongestSubString(line))
            else:
                break
                exit(0)
        except:
            break

