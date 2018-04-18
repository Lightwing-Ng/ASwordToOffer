#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 18, 2018, 11:02 PM
 * Software: PyCharm
 * Project Name: Tutorial
"""

import collections


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        """
        题目描述
        在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2, 3, 1, 0, 2, 5, 3}，那么对应的输出是第一个重复的数字2
        :param numbers:
        :param duplication:
        :return:
        """
        # write code here
        flag = False
        c = collections.Counter(numbers)
        for k, v in c.items():
            if v > 1:
                duplication[0] = k
                flag = True
                break
        return flag

# import random
#
# L = range(1000)
# res = random.sample(L, 5)
#
# res.append(res[1])
# random.shuffle(res)
#
# print(res)
#
# for x in res:
#     if res.count(x) > 1:
#         print(x)
#         break
