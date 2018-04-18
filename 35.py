#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 18, 2018, 4:10 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


class Solution:
    def FirstNotRepeatingChar(self, s):
        """
        题目描述
在一个字符串(1<=字符串长度<=10,000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置
        :param s:
        :return:
        """
        # write code here
        dict = {}
        size = len(s)
        for i in range(size):
            if dict.has_key(s[i]):
                dict[s[i]] = -1
            else:
                dict[s[i]] = i

        min = size - 1
        for key in dict:
            if dict[key] != -1 and dict[key] < min:
                min = dict[key]

        return min
