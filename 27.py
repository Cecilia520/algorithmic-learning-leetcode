#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   27.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/16 15:10   cecilia      1.0         None
"""
import numpy as np


class NMS:
    def calNMS(self, bboxes, threshes):
        """
        计算NMS非极大抑值
        :param bboxes:
        :param threshes:
        :return:
        """
        x1 = bboxes[:, 0]
        y1 = bboxes[:, 1]
        x2 = bboxes[:, 2]
        y2 = bboxes[:, 3]

        scores = bboxes[:, 4]  # 置信度
        area = (y2 - y1 + 1) * (x2 - x1 + 1)
        order = scores.argsort()[::-1]
        final_boxes = []  # final box
        while len(order) > 0:
            i = order[0]  # the box for max score
            final_boxes.append(i)
            xm1 = np.maximum(x1[i], x1[order[1:]])
            ym1 = np.maximum(y1[i], y1[order[1:]])
            xm2 = np.maximum(x2[i], x2[order[1:]])
            ym2 = np.maximum(y2[i], y2[order[1:]])

            width = np.maximum(0, ym2 - ym1 + 1)
            height = np.maximum(0, xm2 - xm1 + 1)

            inter = width * height
            iou_value = inter / (area[i] + area[order[1:]] - inter)
            ids = np.where(iou_value < threshes)[0]
            order = order[ids + 1]
            return final_boxes[0]


if __name__ == '__main__':
    # 0,0,1,3,0.9 0,0,1,2,0.7
    s = NMS()
    threshes = 0.5
    input_list = input().strip().split()
    n = len(input_list)
    bboxes = []
    for i in range(n):
        tmp_list = list(map(float, input_list[i].strip().split(',')))
        bboxes.append(tmp_list)
    print("bboxes:{}".format(bboxes))
    bboxes = np.array(bboxes)
    print(s.calNMS(bboxes, threshes))

