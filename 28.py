#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 17, 2018, 11:34 PM
 * Software: PyCharm
 * Project Name: Tutorial
"""

import collections


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        """
        题目描述
        数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1, 2, 3, 2, 2, 2, 5, 4, 2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
        :param numbers:
        :return:
        """
        # write code here
        temp = collections.Counter(numbers)
        x = len(numbers) / 2
        for k, v in temp.items():
            if v > x:
                return k
        return 0

# import random
#
# key = random.randint(1, 10)
# L = [key for x in range(5)]
#
# while len(L) < 10:
#     temp = random.randint(1, 10)
#     if temp not in L:
#         L.append(temp)
#
# random.shuffle(L)
#
# a = Solution
