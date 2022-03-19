#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   9.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/9/15 20:07   cecilia      1.0         None
"""
import numpy as np

class NMS:
    def calNMS(self,dets, thresh):
        x1 = dets[:, 0]
        y1 = dets[:, 1]
        x2 = dets[:, 2]
        y2 = dets[:, 3]
        scores = dets[:, 4] # 每个预测框的置信度

        area = (y2 - y1 + 1) * (x2 - x1 + 1)
        order = scores.argsort()[::-1] # 降序排列，置信度最高的排在最前面

        keep = [] #keep为最后保留的边框
        while len(order) > 0:
            i = order[0] # order[0]是当前分数最大的窗口，肯定保留
            keep.append(i)

            xx1 = np.maximum(x1[i], x1[order[1:]])
            yy1 = np.maximum(y1[i], y1[order[1:]])
            xx2 = np.minimum(x2[i], x2[order[1:]])
            yy2 = np.minimum(y2[i], y2[order[1:]])
            w = np.maximum(0, yy2 - yy1 + 1)
            h = np.maximum(0, xx2 - xx1 + 1)
            inter = w * h
            iou = inter / (area[i] + area[order[1:]] - inter) # 计算其余所有框与当前框的iou
            ids = np.where(iou < thresh)[0]  #inds为所有与窗口i的iou值小于threshold值的窗口的index
            order = order[ids + 1] # idx + 1的原因：iou数组的长度比order数组的长度少1（不包含i），所以inds+1对应到保留的窗口
        return keep

# # boxes = np.array([[10,10,40,80,0.5],[25,30,70,80,0.9],[30,25,65,78,0.8],[50,50,80,80,0.45]])
# boxes = np.array([[50.0,51.0,180.0,200.0,0.9],[48.0,53.0,170.0,210.1,0.8],[200.0,51.0,242.1,81.0,0.7]])
# res = NMS(boxes, 0.3)
# print(res) # [1, 0, 3]



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

