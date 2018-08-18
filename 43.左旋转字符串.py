# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        return s[n:]+s[:n]# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if s=='':
            return ''
        L=[]
        for i in range(n-1,-1,-1):
            L.append(s[i])
        for i in range(len(s)-1,n-1,-1):
            L.append(s[i])
        return ''.join(L[::-1])