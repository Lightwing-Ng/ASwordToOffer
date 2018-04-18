#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 19, 2018, 5:14 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


class Solution:
    def __init__(self):
        self.vis = {}

    def movingCount(self, k, r, c):
        """
        题目描述
            地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
        :param k: k值
        :param r:
        :param c:
        :return: 
        """
        # write code here
        return self.moving(k, r, c, 0, 0)

    def moving(self, k, r, c, row, col):
        if row / 10 + row % 10 + col / 10 + col % 10 > k:
            return 0
        if row >= r or col >= c or row < 0 or col < 0:
            return 0
        if (row, col) in self.vis:
            return 0
        self.vis[(row, col)] = 1

        return 1 + \
               self.moving(k, r, c, row - 1, col) + \
               self.moving(k, r, c, row + 1, col) + \
               self.moving(k, r, c, row, col - 1) + \
               self.moving(k, r, c, row, col + 1)
