#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Mar 27, 2018, 3:24 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


# 题目描述
# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组
# {3, 4, 5, 1, 2}
# 为
# {1, 2, 3, 4, 5}
# 的一个旋转，该数组的最小值为1。
# NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        pre = -7e20
        for i in rotateArray:
            if i < pre:
                return i
            pre = i

        if len(rotateArray) == 0:
            return 0
        return rotateArray[0]
