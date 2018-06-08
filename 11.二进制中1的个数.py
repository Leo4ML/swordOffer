# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n>=0:
            s=bin(n)[2:]
            return s.count('1')
        else:
            l=len(bin(-n)[2:])+1
            s=bin(n & 0b11111111111111111111111111111111)[2:]
            return s.count('1')