#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 19, 2018, 4:26 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        """
        题目描述
        从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
        :param pRoot:
        :return:
        """
        # write code here
        if not pRoot:
            return []
        res = []
        temp = [pRoot]

        while temp:
            size = len(temp)
            row = []
            for x in temp:
                row.append(x.val)
            res.append(row)

            for x in range(size):
                node = temp.pop(0)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

        return res
