#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 18, 2018, 1:30 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


class Solution:
    def PrintMinNumber(self, numbers):
        """
        题目描述
        输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321,323。
        :param numbers:
        :return:
        """
        # write code here
        if not numbers:
            return ""

        lmb = lambda n1, n2: int(str(n1) + str(n2)) - int(str(n2) + str(n1))
        array = sorted(numbers, cmp=lmb)
        return ''.join([str(i) for i in array])

# import random, itertools
#
# L = []
# N = random.randint(1, 10)
# for x in range(1, N):
#     L.append(random.randint(10 * (x - 1), 10 * x + 1))
#
# print(L)
#
# for x in itertools.permutations(L, N - 1):
#     temp = ''.join(str(x))
