#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Mar 27, 2018, 4:10 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


# 题目描述
# 给定一个double类型的浮点数base和int类型的整数exponent。
# 求base的exponent次方。
class Solution:
    def Power(self, base, exponent):
        # write code here
        flag = 0
        if base == 0:
            return False
        if exponent == 0:
            return 1
        if exponent < 0:
            flag = 1
        result = 1
        for i in range(abs(exponent)):
            result *= base
        if flag == 1:
            result = 1 / result
        return result
