#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Mar 27, 2018, 3:51 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


# 题目描述
# 我们可以用2 * 1的小矩形横着或者竖着去覆盖更大的矩形。
# 请问用n个2 * 1的小矩形无重叠地覆盖一个2 * n的大矩形，总共有多少种方法？

class Solution:
    def rectCover(self, N):
        # write code here
        if N < 0:
            return 0
        else:
            p, q, res = 0, 0, 0
            for i in range(1, N + 1):
                if i == 1:
                    p = q = res = 1
                elif i == 2:
                    q = res = 2
                else:
                    res = p + q
                    p = q
                    q = res
            return res
