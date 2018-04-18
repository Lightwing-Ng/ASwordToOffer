#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 18, 2018, 10:43 PM
 * Software: PyCharm
 * Project Name: Tutorial
"""


class Solution:
    def Add(self, N1, N2):
        """
        题目描述
        写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号
        :param num1:
        :param num2:
        :return:
        """
        # write code here
        s = [N1, N2]
        return sum(s)
