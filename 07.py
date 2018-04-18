#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Mar 27, 2018, 3:29 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


# 题目描述
# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
# n <= 39

class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        else:
            res = [] * n
            res.append(1)
            res.append(1)
            for i in xrange(2, n):
                res.append(res[i - 1] + res[i - 2])
            return res[n - 1]



