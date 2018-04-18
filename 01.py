#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Mar 27, 2018, 1:47 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


# 二维数组中的查找
# 题目描述
# 在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

# Input:
#     2
#     1 2
#     3 4


class Solution:
    # array as a argument
    def Find(self, target, array):
        # write code here
        n = len(array)
        flag = 'false'
        for i in range(n):
            if target in array[i]:
                flag = 'true'
                break
        return flag


while True:
    try:
        S = Solution()
        # Trans the strings to a List
        L = list(eval(raw_input()))
        array = L[1]
        target = L[0]
        print(S.Find(target, array))
    except:
        break
