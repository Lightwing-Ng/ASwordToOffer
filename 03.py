#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Mar 27, 2018, 2:10 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        l = []
        head = listNode
        while head:
            l.insert(0, head.val)
            head = head.next
        return l

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# import random
#
# s = ListNode
# for i in range(100):
#     x = random.random()
#     s(x)
