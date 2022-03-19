#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   LengthOfLongestSubstring.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/8/21 18:12   cecilia      1.0        最长不含重复字符的子字符串
问题描述：
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

 

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
'''
思路分析：
方法一：动态规划+哈希表——时间复杂度O（N），空间复杂度O（1）
dp[j]表示以字符s[j]结尾的“最长无重复字符串”长度
固定j,设s[j]字符左边距离最近的相同字符s[i]，s[j] = s[i]；
当i<0,表示左边没有字符，此时dp[j] dp[j - 1] + 1;
当dp[j-1] < j - i,表示s[i]字符在子字符串dp[j-1]区间之外，dp[j]=dp[j-1] + 1;
当dp[j-1] >= j - i,表示s[i]在子字符串dp[j-1]区间之内，dp[j] = j - i
按照这样分析来看，需要遍历两次，时间复杂度为O（N^2）,空间复杂度为O（1），此时可以使用哈希表来优化——
哈希表存储重复字符的索引位置

方法二：双指针（滑动窗口）+ 哈希表——时间复杂度O（N）,空间复杂度O（1）
使用哈希表记录每个字符的下一个索引，然后尽量向右移动尾指针来拓展窗口，并更新窗口的最大长度。如果尾指针指向的元素重复，则将头指针直接移动到窗口中重复元素的右侧。

'''
class Solution:
    def LengthOfLongestSubstring(self, s: str)-> int:
        """
        计算无重复字符串的最大长度
        方法一：动态规划+哈希表
        :param s:
        :return:
        """
        res = 0
        dic = {}
        tmp = 0
        for j in range(1, len(s)):
            # 记录当前的重复字符的索引位置
            i = dic.get(s[j], -1)
            # 更新索引
            dic[s[j]] = j
            tmp = tmp + 1 if tmp < j - i else j - i
            res = max(res, tmp)
        return res

    def LengthOfLongestSubstringByDoublePointer(self, s: str)->int:
        """
        计算无重复字符串的最大长度
        方法一：双指针+哈希表
        :param s:
        :return:
        """
        dic = {}
        res = 0
        i = -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i)
            dic[s[j]] = j
            res = max(res, (j - i))
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.LengthOfLongestSubstring("abcabcbb"))
    print(s.LengthOfLongestSubstringByDoublePointer("abcabcbb"))