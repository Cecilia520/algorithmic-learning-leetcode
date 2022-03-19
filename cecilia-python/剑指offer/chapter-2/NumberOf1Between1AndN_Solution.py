#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   NumberOf1Between1AndN_Solution.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/9 10:11   cecilia      1.0       从0-n之间的整数中1出现的次数
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。

例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

 

示例 1：

输入：n = 12
输出：5
示例 2：

输入：n = 13
输出：6
 

限制：

1 <= n < 2^31

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
'''
思路分析：
关键点在于使用数学逻辑推导出高位、低位和当前位的中1出现的次数关系，然后使用递归解决问题
'''


class Solution:
    def NumberOf1Between1AndN_Solution(self, n: int) -> int:
        """
        统计从0-n整数中1出现的次数
        :param n:
        :return:
        复杂度分析：时间复杂度O(logN),空间复杂度O(1)
        """
        res, digit = 0, 1
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            if cur == 0:
                res += high * digit  # eg.0010-2304,高位0010-2219，000-229，229-0+1=230=23*10
            elif cur == 1:
                res += high * digit + low + 1  # 比如0010-2314，高位0-234，234-0+1=23*10+4+1
            else:
                res += (high + 1) * digit  # eg. 2359, 0010-239,高位239-0+1=（23+1）*10
            low += cur * digit  # 将cur计入low中
            cur = high % 10
            high //= 10
            digit *= 10
        return res


if __name__ == '__main__':
    n = int(input())
    s = Solution()
    print(s.NumberOf1Between1AndN_Solution(n))
