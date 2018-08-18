# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        k=1
        ans=[]
        while k<=len(array):
            res=[]
            for i in range(len(array)-k+1):
                res.append(sum(array[i:i+k]))
            ans.append(max(res))
            k+=1
        return max(ans)