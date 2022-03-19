#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ValidateStackSequences.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/8/20 13:48   cecilia      1.0       验证栈的元素序列是否正确
问题描述：
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

示例 1：

输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
示例 2：

输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
输出：false
解释：1 不能在 2 之前弹出。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def validateStackSequences(self, pushed: List[int], poped:List[int])->bool:
        """
        验证栈元素序列是否正确
        :param pushed:
        :param poped:
        :return:
        时间复杂度O（N），空间复杂度O（N）
        """
        help_stack, i = [], 0
        for num in pushed:
            help_stack.append(num)
            while help_stack and help_stack[-1] == poped[i]:
                help_stack.pop()
                i += 1
        return not help_stack
