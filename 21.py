#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 01, 2018, 12:45 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


# 题目描述
# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。
# 例如序列1, 2, 3, 4, 5
# 是某栈的压入顺序，序列4, 5, 3, 2, 1
# 是该压栈序列对应的一个弹出序列，但
# 4, 3, 5, 1, 2
# 就不可能是该压栈序列的弹出序列。
# （注意：这两个序列的长度是相等的）

class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or len(pushV) != len(popV):
            # 出入序列不相等
            return False

        stack = []
        for i in pushV:
            stack.append(i)
            while len(stack) and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)

        if len(stack):
            return False

        return True
