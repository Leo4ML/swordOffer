# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        l=[1,2,3]
        if number<=3:
            return number
        else:
            for i in range(3,number):
                l.append(l[i-2]+l[i-1])
            return l[-1]