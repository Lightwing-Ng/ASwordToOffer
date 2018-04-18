#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Mar 27, 2018, 2:03 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""


# 替换空格

# 请实现一个函数，将一个字符串中的空格替换成“%20”。
# 例如，当字符串为
# We Are Happy.
# 则经过替换之后的字符串为
# We%20Are%20Happy。

class Solution:
    def replaceSpace(self, s):
        s = list(s)  # 列表化
        N = len(s)  # 字符串长度
        for i in range(0, N):
            if s[i] == ' ':
                s[i] = '%20'
        return ''.join(s)

# s = 'If this is your first time using Django, you’ll have to take care of some initial setup. Namely, you’ll need to auto-generate some code that establishes a Django project – a collection of settings for an instance of Django, including database configuration, Django-specific options and application-specific settings.'
#
# a = Solution()
# print(a.replaceSpace(s))
