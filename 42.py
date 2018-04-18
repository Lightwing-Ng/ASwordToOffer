#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 18, 2018, 5:35 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


class Solution:
    def FindContinuousSequence(self, s):
        """
        题目描述
        小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
        输出描述:
        输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
        :param s:
        :return:
        """
        # write code here
        if s == 1:
            return []
        d = 2
        res = []
        while d:
            if d % 2 == 1:
                if s % d == 0:
                    res = [
                        x for x in range(
                            int(s // d - (d - 1) / 2),
                            int(s // d + (d - 1) / 2) + 1
                        )
                    ]
                    break
            else:
                if s % 2 == 1:
                    res = [
                        x for x in range(
                            int(s // d - d / 2 + 1),
                            int(s // d + d / 2) + 1
                        )
                    ]
                    break
            d += 1
        return res

# import random
#
# s = random.randint(1, 1000)
# print(s)
# d = 2
# res = []
# while d:
#     if d % 2 == 1:
#         if s % d == 0:
#             res = [
#                 x for x in range(
#                     int(s // d - (d - 1) / 2),
#                     int(s // d + (d - 1) / 2) + 1
#                 )
#             ]
#             break
#     else:
#         if s % 2 == 1:
#             res = [
#                 x for x in range(
#                     int(s // d - d / 2 + 1),
#                     int(s // d + d / 2) + 1
#                 )
#             ]
#             break
#     d += 1
#
# print(res)
