# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        left=1
        right=1
        if n==0:
            return 0
        if n<=2:
            return left
        while n>2:
            left=left+right
            right=left+right
            n=n-2
        if n%2==1:
            return left
        if n%2==0:
            return right