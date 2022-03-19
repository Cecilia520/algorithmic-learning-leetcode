#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ExchangeOddAndDouble.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/8/4 17:32   cecilia      1.0        交换数组的奇数和偶数的顺序
问题描述：
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
import collections

'''
面对这道题，可以有两个思路提供——
第一，使用双端队列的方式，遍历数组，如果该元素是奇数，加入队首，反之加入队尾；
第二，不适用额外的空间，使用快慢指针的方式遍历数组，如果遇到快指针和慢指针的元素分别是偶数和奇数，则交换；否则指针++
'''
class Solution:
    def exchangeOddAndDouble(self, nums: List[int])->List[int]:
        """
        交换数组的奇数和偶数顺序（双端队列法）
        :param nums:
        :return:
        复杂度分析：时间复杂度O（n），空间复杂度O（n）
        """
        queue = collections.deque()
        for num in nums:
            if num & 1 == 0: # 当前元素是偶数
                queue.append(num)
            else:
                queue.appendleft(num)
        return list(queue)

if __name__ == '__main__':
    s = Solution()
    print(s.exchangeOddAndDouble(nums=[1,2,3,4]))