#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 18, 2018, 6:35 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""

import itertools


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        """
        题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，是的他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
输出描述:
对应每个测试案例，输出两个数，小的先输出。
        :param array:
        :param tsum:
        :return:
        """
        # write code here
        res = []
        if not isinstance(array, list):
            return res

        for i, v in enumerate(array):
            for v1 in array[i:]:
                if (v + v1) == tsum:
                    res.append([v, v1])

        if res:
            return res[0]
        else:
            return res
        # res = []
        # min = 0
        # for x in itertools.combinations(A, 2):
        #     if x[0] + x[1] == S:
        #         res.append(x)
        #         min = x[0] * x[1]
        # 
        # a, b = 0, 0
        # for x in res:
        #     if x[0] * x[1] <= min:
        #         a, b = x[0], x[1]
        # 
        # return a, b

# import random, itertools
#
# L = []
# N = random.randint(3, 11)
# print(N)
# while len(L) < N:
#     temp = random.randint(1, 100)
#     if temp not in L:
#         L.append(temp)
# L.sort()
# print(L)
# s = L[random.randint(0, N - 1)] * L[random.randint(0, N - 1)]
# res = []
# for x in itertools.combinations(L, 2):
#     if x[0] * x[1] == s:
#         res.append(x)
#
# print(res)
