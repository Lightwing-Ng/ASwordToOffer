#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 19, 2018, 2:37 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        """
        题目描述
一个链表中包含环，请找出该链表的环的入口结点。
        :param pHead:
        :return:
        """
        # write code here
        tempList = []
        p = pHead

        while p:
            if p in tempList:
                return p
            else:
                tempList.append(p)
            p = p.next