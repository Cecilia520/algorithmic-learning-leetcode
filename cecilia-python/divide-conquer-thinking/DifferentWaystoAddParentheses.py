#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   DifferentWaystoAddParentheses.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/17 17:05   cecilia      1.0       给不同的表达式添加括号（ 为运算表达式设计优先级）
问题描述：
给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。

示例 1:
输入: "2-1-1"
输出: [0, 2]
解释:
((2-1)-1) = 0
(2-(1-1)) = 2

示例 2:
输入: "2*3-4*5"
输出: [-34, -14, -10, -10, 10]
解释:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10

思路分析：
1. 分解。根据运算符将问题分解成多个独立的子问题。
2. 求解。构造一个递归函数，输入算式，即可求解。
3. 合并。根据运算符将左右两边的算式解进行合并起来，得到最终问题的整体解。
"""


def differentWaystoAddParentheses(input):
    """
    为算术表达式设计优先级，即添加括号
    :param input: 输入算式表达式
    :return:
    """
    # 判断输入值是否是数字或者只有数字
    if input.isdigit():
        return [int(input)]

    answer = []

    for i, char in enumerate(input):
        # 分解。如果遇到运算符，则计算左右两边的结果
        if char in ['+', '-', '*']:
            left = differentWaystoAddParentheses(input[:i])
            right = differentWaystoAddParentheses(input[i + 1:])
            print("left:{}, right:{}".format(left, right))
            # 求解。递归求出问题的子集。
            # 合并。
            for l in left:
                for r in right:
                    if char == '+':
                        answer.append(l + r)
                    elif char == '-':
                        answer.append(l - r)
                    else:
                        answer.append(l * r)
    return answer


if __name__ == '__main__':
    input = "2-1-1"
    # input = "2*3-4*5"
    print(differentWaystoAddParentheses(input))
