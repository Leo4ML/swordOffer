# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        L=[]
        c=0
        for i in pushV:
            if i !=popV[c]:
                L.append(i)
            else:
                c+=1
                
        if popV[c:]==L[::-1]:
            return True
        else:
            return False