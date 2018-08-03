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
    
'''
还可以这么简单，且不用额外空间！
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        maxsum,cursum=array[0],array[0]
        for i in array[1:]:
            cursum=max(cursum+i,i)
            maxsum=max(maxsum,cursum)
        return maxsum
'''