#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 18, 2018, 5:30 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


class Solution:
    # 返回[a, b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        """
        题目描述
        一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
        :param array:
        :return:
        """
        # write code here
        res = []
        for x in array:
            if array.count(x) == 1:
                res.append(x)
        return res
