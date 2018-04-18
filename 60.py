#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 19, 2018, 4:22 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        """
        题目描述
        请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
        :param pRoot:
        :return:
        """
        # write code here
        result = []
        stack = [pRoot]
        level = 1

        while len(stack) > 0:
            ns, rs = [], []

            for x in stack:
                if x != None:
                    rs.append(x.val)
                    if x.left != None:
                        ns.append(x.left)
                    if x.right != None:
                        ns.append(x.right)

            if level % 2 == 0:
                rs.reverse()
            if len(rs) > 0:
                result.append(rs)

            stack = ns
            level += 1
        return result
