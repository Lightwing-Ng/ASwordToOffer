#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 19, 2018, 4:39 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        """
        题目描述
给定一颗二叉搜索树，请找出其中的第k大的结点。例如，
     5
   /  \
  3   7
 /\  /\
2 4 6 8
中，按结点数值大小顺序第三个结点的值为4。
        :param pRoot:
        :param k:
        :return:
        """
        # write code here
        global result
        result = []
        self.midnode(pRoot)
        if k <= 0 or len(result) < k:
            return None
        else:
            return result[k - 1]

    def midnode(self, root):
        if not root:
            return None
        self.midnode(root.left)
        result.append(root)
        self.midnode(root.right)
