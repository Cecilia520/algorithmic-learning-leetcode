#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   23.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/13 9:52   cecilia      1.0         None

现有一种特殊的3D矩阵乘法：

    ①：有两个3D矩阵A、B，形状分别为5*2*2、2*2*2；一个列表M，M中的元素为0或1，长度为5。

    ②：从3D矩阵A中依次抽取2D子矩阵A_slice，即5个2*2矩阵。

    ③：从3D矩阵B中依次抽取2D子矩阵B_slice，即2个2*2矩阵。

    ④：将列表M的元素作为下标，依次从③中拷贝5次B_slice（0为第一个2*2矩阵，1为第二个2*2矩阵）。

    ⑤：①与④的5个子矩阵两两进行矩阵乘法（A_slices[i]*B_slices[M[i]]），最后对所有结果（2D矩阵）进行依次拼接为一个3D矩阵（大小为5*2*2），记为Y。

给定A、B、M与传导至此的梯度D（大小同Y，5*2*2），求A、B、M的梯度dA、dB、dM。
"""
#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


class Matrix:
    def __init__(self, shape, data: list):
        self.shape = shape
        self.data = data
        self.length = self.shape[0] * self.shape[1]

    def _verify(self, location):
        assert location[0] < self.shape[0] and location[1] < self.shape[1]

    def __getitem__(self, location):
        self._verify(location)
        return self.data[location[0] * self.shape[1] + location[1]]

    def __setitem__(self, location, value: int):
        self._verify(location)
        self.data[location[0] * self.shape[1] + location[1]] = value

    def transpose(self):
        transposed_data = [self.data[i * self.shape[1] + j] for j in range(self.shape[1]) for i in range(self.shape[0])]
        return Matrix((self.shape[1], self.shape[0]), transposed_data)

    def reshape(self, shape):
        self.shape = shape

    @staticmethod
    def matmul(ma, mb):
        assert ma.shape[1] == mb.shape[0]
        mc = Matrix.zeros((ma.shape[0], mb.shape[1]))
        for i in range(mc.shape[0]):
            for j in range(mc.shape[1]):
                mc[i, j] = sum([ma[i, k] * mb[k, j] for k in range(ma.shape[1])])
        return mc

    def __add__(self, other):
        if isinstance(other, int):
            return Matrix(self.shape, [value + other for value in self.data])
        elif isinstance(other, Matrix):
            return Matrix(self.shape, [self.data[i] + other.data[i] for i in range(self.length)])

    def __sub__(self, other):
        if isinstance(other, int):
            return Matrix(self.shape, [value - other for value in self.data])
        elif isinstance(other, Matrix):
            return Matrix(self.shape, [self.data[i] - other.data[i] for i in range(self.length)])

    def __mul__(self, other):
        if isinstance(other, int):
            return Matrix(self.shape, [value * other for value in self.data])
        elif isinstance(other, Matrix):
            return Matrix(self.shape, [self.data[i] * other.data[i] for i in range(self.length)])

    @staticmethod
    def zeros(shape):
        return Matrix(shape, [0 for _ in range(shape[0] * shape[1])])

    @staticmethod
    def ones(shape):
        return Matrix(shape, [1 for _ in range(shape[0] * shape[1])])

    def print(self):
        print(",".join([str(i) for i in self.data]))


class Matrix3D:
    def __init__(self, shape, data: list):
        self.shape = shape
        self.data = data
        self.length = self.shape[0] * self.shape[1] * self.shape[2]

    def _verify(self, location):
        assert location[0] < self.shape[0] and location[1] < self.shape[1] and location[2] < self.shape[2]

    def __getitem__(self, location):
        self._verify(location)
        return self.data[location[0] * (self.shape[1] * self.shape[2]) + location[1] * self.shape[2] + location[2]]

    def __setitem__(self, location, value: int):
        self._verify(location)
        self.data[location[0] * (self.shape[1] * self.shape[2]) + location[1] * self.shape[2] + location[2]] = value

    def get_2D_slice(self, index):
        offset = self.shape[1] * self.shape[2]
        loc = index * offset
        return Matrix((self.shape[1], self.shape[2]), self.data[loc:loc + offset])

    def reshape(self, shape):
        self.shape = shape

    @staticmethod
    def zeros(shape):
        return Matrix3D(shape, [0 for _ in range(shape[0] * shape[1] * shape[2])])

    @staticmethod
    def ones(shape):
        return Matrix3D(shape, [1 for _ in range(shape[0] * shape[1] * shape[2])])

    def print(self):
        print(",".join([str(i) for i in self.data]))


def mix_matmul(A: Matrix3D, B: Matrix3D, M: list):
    data_of_result = []
    shape_of_result = (A.shape[0], A.shape[1], B.shape[2])
    for i, index_of_slice in enumerate(M):
        A_slice = A.get_2D_slice(i)
        B_slice = B.get_2D_slice(index_of_slice)
        Y_slice = Matrix.matmul(A_slice, B_slice)
        data_of_result.extend(Y_slice.data)
    return Matrix3D(shape_of_result, data_of_result)


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def d_mix_matmul(A: Matrix3D, B: Matrix3D, M: list, D: Matrix3D):
    dA, dB, dM = Matrix3D.zeros(A.shape), Matrix3D.zeros(B.shape), Matrix.zeros((1, len(M)))
    # 完成具体梯度计算并将结果存入上方申请的结果矩阵中
    mA, nA = A.shape
    mB, nB = B.shape
    mC, nC = M.shape



    # 结束具体梯度计算
    dA.print()
    dB.print()
    dM.print()


# ******************************结束写代码******************************


if __name__ == '__main__':
    A = Matrix3D((5, 2, 2), [int(i) for i in input().split(",")])
    B = Matrix3D((2, 2, 2), [int(i) for i in input().split(",")])
    M = [int(i) for i in input().split(",")]
    D = Matrix3D((5, 2, 2), [int(i) for i in input().split(",")])
    d_mix_matmul(A, B, M, D)
