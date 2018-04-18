#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 19, 2018, 2:51 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        """
        题目描述
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
        :param pNode:
        :return:
        """
        # write code here
        if not pNode:
            return pNode

        if pNode.right:
            left_1 = pNode.right
            while left_1.left:
                left_1 = left_1.left
            return left_1

        p = pNode

        while pNode.next:
            temp = pNode.next
            if temp.left == pNode:
                return temp
            pNode = temp
