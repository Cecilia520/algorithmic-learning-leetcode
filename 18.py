#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   18.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/16 16:31   cecilia      1.0         None
"""
class IOU:
    def cal_iou(self, l1, l2)->int:
        """
        计算两个矩形的交并比
        :param l1:
        :param l2:
        :return:
        """
        x1, y1, w1, h1 = l1
        x2, y2, w2, h2 = l2

        lw = (w1 + w2) - (max(x1 + w1, x2 + w2) - min(x1, x2))
        lh = (h1 + h2) - (max(y1 + h1, y2 + h2) - min(y1, y2))

        # 如果相交区域面积为0
        if lh <= 0 or lw <= 0:
            return 0
        s = lw * lh
        b = w1 * h1 + w2 * h2 - s
        return s / b

    def cal_iou2(self, l1, l2)->int:
        """
        计算两个矩形的交并比
        :param l1:
        :param l2:
        :return:
        """
        x1, y1, w1, h1 = l1
        x2, y2, w2, h2 = l2

        l1_area = max(y)

if __name__ == '__main__':
    s = IOU()
    # 0.0,0.0,1.0,1.0 0.0,0.0,0.5,1.0
    input_list = input().strip().split()
    l1 = list(map(float, input_list[0].strip().split(',')))
    l2 = list(map(float, input_list[1].strip().split(',')))
    print(s.cal_iou(l1, l2))