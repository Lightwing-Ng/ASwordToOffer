#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 18, 2018, 5:11 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


class Solution:
    def GetNumberOfK(self, data, k):
        """
        题目描述
        统计一个数字在排序数组中出现的次数。
        :param data:
        :param k:
        :return:
        """
        # write code here
        return data.count(k)
