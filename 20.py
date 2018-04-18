#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Mar 31, 2018, 11:32 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


# 题目描述
# 定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。

class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.min_stack or node <= self.min_stack[-1]:
            self.min_stack.append(node)

    def pop(self):
        # write code here
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        # write code here
        return self.stack[-1]

    def min(self):
        # write code here
        return self.min_stack[-1]
