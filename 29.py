#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 18, 2018, 12:28 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        """
        题目描述
        输入n个整数，找出其中最小的K个数。例如输入4, 5, 1, 6, 2, 7, 3, 8这8个数字，则最小的4个数字是1, 2, 3, 4,。
        :param tinput:
        :param k:
        :return:
        """
        # write code here
        if tinput is None:
            return

        n = len(tinput)
        if n < k:
            return []

        tinput = sorted(tinput)
        return tinput[:k]
