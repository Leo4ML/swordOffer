# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        res=[]
        l=list(ss)
        if len(ss)==1:
            res.append(l)
            return list(ss)
            #break
        #if len(ss)==2:
            #res.append(l)
            #res.append(l[::-1])
        if len(ss)>=2:
            #s=[]
            for i in range(len(l)):
                s=[]
                s.append(l[i])
                del l[i]
                s+self.Permutation(str(l))
        return res
s=Solution()
print s.Permutation('abc')
            