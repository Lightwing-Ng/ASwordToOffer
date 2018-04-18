#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Mar 31, 2018, 2:05 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        l = []
        while head != None:
            l.append(head)
            head = head.next

        if k > len(l) or k < 1:
            return

        return l[-k]
