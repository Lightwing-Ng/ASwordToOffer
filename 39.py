#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 18, 2018, 5:13 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        """
        题目描述
        输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
        :param pRoot:
        :return:
        """
        # write code here
        if not pRoot:
            return 0
        return max(
            1 + self.TreeDepth(pRoot.left),
            1 + self.TreeDepth(pRoot.right)
        )
