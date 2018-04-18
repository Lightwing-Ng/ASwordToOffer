#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 18, 2018, 2:15 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


class Solution:
    def GetUglyNumber_Solution(self, index):
        """
        题目描述
        把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
        :param index:
        :return:
        """
        # write code here
        if index <= 0:
            return 0
        uglyList = [1]
        TWO, THREE, FIVE = 0, 0, 0

        for i in range(index - 1):
            newUgly = min(
                uglyList[TWO] * 2,
                uglyList[THREE] * 3,
                uglyList[FIVE] * 5
            )
            uglyList.append(newUgly)

            if newUgly % 2 == 0:
                TWO += 1
            if newUgly % 3 == 0:
                THREE += 1
            if newUgly % 5 == 0:
                FIVE += 1

        return uglyList[-1]
