#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 18, 2018, 5:06 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        list1, list2 = [], []
        node1, node2 = pHead1, pHead2

        while node1:
            list1.append(node1.val)
            node1 = node1.next

        while node2:
            if node2.val in list1:
                return node2
            else:
                node2 = node2.next
