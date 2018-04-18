#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Mar 27, 2018, 3:45 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


# 题目描述
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法。

class Solution:
    def jumpFloor(self, N):
        # write code here
        x, y = 1, 1
        for i in range(N):
            x, y = y, x + y
        return x
