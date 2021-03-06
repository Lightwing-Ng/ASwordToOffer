#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 18, 2018, 11:38 PM
 * Software: PyCharm
 * Project Name: Tutorial
"""


class Solution:
    """
    题目描述
    请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
输出描述:
    如果当前字符流没有存在出现一次的字符，返回#字符。
    """

    def __init__(self):
        # 返回对应char
        self.s = ''
        self.dict1 = {}

    def FirstAppearingOnce(self):
        # write code here
        for x in self.s:
            if self.dict1[x] == 1:
                return x
        return '#'

    def Insert(self, char):
        # write code here
        self.s = self.s + char
        if char in self.dict1:
            self.dict1[char] = self.dict1[char] + 1
        else:
            self.dict1[char] = 1
