#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Mar 27, 2018, 3:59 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


# 题目描述
# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

class Solution:
    def NumberOf1(self, n):
        # write code here
        return sum(
            [
                (n >> i & 1) for i in range(0, 32)
            ]
        )
