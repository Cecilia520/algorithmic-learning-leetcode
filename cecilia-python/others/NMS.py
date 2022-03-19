a#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   NMS.py
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/9/15 20:10   cecilia      1.0        实现NMS非极大值抑制算法

3 0.3
50.0 51.0 180.0 200.0 0.9
48.0 53.0 170.0 210.1 0.8
200.0 51.0 242.1 81.0 0.7
样例输出
50.0 51.0 180.0 200.0 0.9
200.0 51.0 242.1 81.0 0.7
"""
import numpy as np
class NMS:
    def calNMS(self, bboxes, threshes):
        """
        NMS非极大抑制
        :param bboxes:
        :param threshes:
        :return:
        """
        x1 = bboxes[:, 0]
        y1 = bboxes[:, 1]
        x2 = bboxes[:, 2]
        y2 = bboxes[:, 3]
        scores = bboxes[:, 4] # 每个预测框的置信度

        area = (y2 - y1 + 1) * (x2 - x1 + 1)
        order = scores.argsort()[::-1] # 降序排列，置信度最高的排在最前面

        final_boxes = [] # 保留最后留下来的边框
        while len(order) > 0:
            i = order[0] # the boxes for max score
            final_boxes.append(i)

            xm1 = np.maximum(x1[i], x1[order[1:]])
            ym1 = np.maximum(y1[i], y1[order[1:]])
            xm2 = np.maximum(x2[i], x2[order[1:]])
            ym2 = np.maximum(y2[i], y2[order[1:]])
            width = np.maximum(0, ym2 - ym1 + 1)
            height = np.maximum(0, xm2 - xm1 + 1)
            inter = width * height
            iou = inter / (area[i] + area[order[1:]] - inter) # 计算其余所有框与当前框的iou
            ids = np.where(iou < threshes)[0] #inds为所有与窗口i的iou值小于threshold值的窗口的index
            order = order[ids + 1] # # idx + 1的原因：iou数组的长度比order数组的长度少1（不包含i），所以inds+1对应到保留的窗口
        return final_boxes

if __name__ == '__main__':
    s = NMS()
    input_list = input().strip().split()
    n = int(input_list[0])
    threshes = float(input_list[1]) # 阈值
    bboxes = []
    for i in range(n):
        tmp_list = list(map(float, input().strip().split()))
        bboxes.append(tmp_list)
    bboxes = np.array(bboxes)
    print(s.calNMS(bboxes, threshes))


