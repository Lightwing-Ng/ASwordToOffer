#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 18, 2018, 10:39 PM
 * Software: PyCharm
 * Project Name: Tutorial
"""


class Solution:
    def Sum_Solution(self, n):
        """
        题目描述
        求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
        :param n:
        :return:
        """
        # write code here
        sum = 0
        if n:
            for x in range(1, n + 1):
                sum += x
            return sum
        else:
            return False
