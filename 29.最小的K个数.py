# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        res=[]
        if len(tinput)<k:
            return res
        else:
            while k!=0:
                m=sorted(tinput)[0]
                tinput.remove(m)
                res.append(m)
                k-=1
            return res