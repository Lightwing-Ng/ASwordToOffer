#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Mar 27, 2018, 2:22 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


# 题目描述
# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列
# {1, 2, 4, 7, 3, 5, 6, 8}
# 和中序遍历序列
# {4, 7, 2, 1, 5, 3, 8, 6}，则重建二叉树并返回。

# 测试用例：
# 输入
# [1, 2, 3, 4, 5, 6, 7], [3, 2, 4, 1, 6, 5, 7]
# 输出一个TreeNode:
#       1
#    /    \
#   2      5
#  / \    / \
# 3   4  6   7


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            # 先序遍历仅有一个元素，列表即本身
            return TreeNode(pre[0])
        else:
            # 用中序遍历递归访问前续和后续的左右结点
            flag = TreeNode(pre[0])
            # 先找根节点左边
            # 将待定根节点的左子树的前序遍历，后续便利递归进
            flag.left = self.reConstructBinaryTree(
                pre[1:tin.index(pre[0]) + 1],
                tin[:tin.index(pre[0])]
            )
            # 将待定根节点的左子树的前序遍历，后续便利递归进
            flag.right = self.reConstructBinaryTree(
                pre[tin.index(pre[0]) + 1:],
                tin[tin.index(pre[0]) + 1:]
            )

        return flag


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#
# s = Solution()
# pre = [1, 2, 3, 4, 5, 6, 7]
# tin = [3, 2, 4, 1, 6, 5, 7]
#
# flag = pre[0]
# print('前序遍历：%s.' % pre)
# print('中序遍历：%s.' % tin)
# print('第一轮的根节点为：%s.' % flag)
#
# print(pre[1:tin.index(pre[0]) + 1])
# print(tin[:tin.index(pre[0])])
# print('\n')
# print(pre[tin.index(pre[0]) + 1:])
# print(tin[tin.index(pre[0]) + 1:])
