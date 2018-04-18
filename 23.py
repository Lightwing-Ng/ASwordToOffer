#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 17, 2018, 11:14 PM
 * Software: PyCharm
 * Project Name: Tutorial
"""


class Solution:
    """
    题目描述
    输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
        10
       / \
      9   8
     / \   \
    7   6   5
       / \  / \
      4   3 2  1
    """

    def VerifySquenceOfBST(self, sequence):
        # 初始序列
        # 7 -> 4 -> 3 -> 6 -> 9, 2 -> 1 -> 5 -> 8, 10
        # write code here
        lenSeq = len(sequence)
        if lenSeq == 0:
            return False
        if lenSeq == 1:
            return True
        root = sequence[-1]
        # 假定每个序列的最后一个为根节点
        left = 0
        while sequence[left] < root:
            left += 1
        for j in range(left, lenSeq - 1):
            if sequence[j] < root:
                return False

        # left为分割左右的坐标
        return self.VerifySquenceOfBST(sequence[:left]) or self.VerifySquenceOfBST(sequence[left:length - 1])
