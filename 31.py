#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 18, 2018, 12:59 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        """
        题目描述
        求出1~13的整数中1出现的次数,并算出100 ~ 1300的整数中1出现的次数？为此他特别数了一下1 ~ 13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他，并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数。
        :param n:
        :return:
        """
        # write code here
        res = 0
        tmp = n
        base = 1
        while tmp:
            last = tmp % 10
            tmp = tmp / 10
            res += tmp * base

            if last == 1:
                res += n % base + 1
            elif last > 1:
                res += base
            base *= 10
        return res
