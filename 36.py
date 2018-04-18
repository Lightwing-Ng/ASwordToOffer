#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 18, 2018, 4:32 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""

import random
import itertools


class Solution:
    def InversePairs(self, data):
        """
        题目描述
        在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
        输入描述:
        题目保证输入的数组中没有的相同的数字
        数据范围：
	        对于%50的数据,size<=10^4
	        对于%75的数据,size<=10^5
	        对于%100的数据,size<=2*10^5
        示例1
        输入
            1, 2 ,3, 4, 5, 6, 7, 0
        输出
            7
        :param data:
        :return:
        """
        # write code here
        data = [1, 2, 3, 4, 5, 6, 7, 0]
        sum = 0
        for x in range(0, len(data) - 2):
            for y in range(x + 1, len(data) - 1):
                if data[x] > data[y]:
                    sum += 1
        return sum

        # res = 0
        # for x in itertools.combinations(data, 2):
        #     if x[0] > x[1]:
        #         res += 1
        # return res


# testNum = []
# for x in range(500):
#     testNum.append(random.randint(0, 10 ** 4 + 1))
# for x in range(250):
#     testNum.append(random.randint(10 ** 4, 10 ** 5 + 1))
# for x in range(250):
#     testNum.append(random.randint(10 ** 5 + 1, 2 * 10 ** 5 + 1))
#
# random.shuffle(testNum)
#
# sum = 0
# for x in itertools.combinations([1, 2, 3, 4, 5, 6, 7, 0], 2):
#     if x[0] > x[1]:
#         sum += 1
#
# print(format(sum, ','))

data = [1, 2, 3, 4, 5, 6, 7, 0]
sum = 0
for x in range(0, len(data) - 2):
    for y in range(x + 1, len(data) - 1):
        if data[x] > data[y]:
            sum += 1
print(sum)
