#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 18, 2018, 11:12 PM
 * Software: PyCharm
 * Project Name: Tutorial
"""


class Solution:
    def multiply(self, A):
        """
        题目描述
        给定一个数组A[0, 1, ..., n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
        :param A:
        :return:
        """
        # write code here
        if not A:
            return []

        N = len(A)
        B = [None] * N
        B[0] = 1
        for i in range(1, N):
            B[i] = B[i - 1] * A[i - 1]

        temp = 1
        for i in range(N - 2, -1, -1):
            temp *= A[i + 1]
            B[i] *= temp
        return B
