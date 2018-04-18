#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 18, 2018, 11:31 PM
 * Software: PyCharm
 * Project Name: Tutorial
"""


class Solution:
    # s字符串
    def isNumeric(self, s):
        """
        题目描述
        请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
        :param s:
        :return:
        """
        # write code here
        try:
            p = float(s)
            return True
        except:
            return False
