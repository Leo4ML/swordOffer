# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        odd=[]
        even=[]
        for i in array:
            if i%2==0:
                even.append(i)
            if i%2==1:
                odd.append(i)
        return odd+even