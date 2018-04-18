#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 17, 2018, 11:20 PM
 * Software: PyCharm
 * Project Name: Tutorial
"""

import itertools


class Solution:
    def Permutation(self, ss):
        """
        题目描述
        输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
        :param ss:
        :return:
        """
        # write code here
        if not ss:  # 若字符串不为空
            return []
        return sorted(
            list(
                set(
                    map(''.join, itertools.permutations(ss))
                )
            )
        )
