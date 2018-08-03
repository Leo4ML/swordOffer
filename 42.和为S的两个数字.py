# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        res=[]
        k=0
        while k <=len(array)-2:
            for i in range(k+1,len(array)):
                if array[k]+array[i]==tsum:
                    if res==[]:
                        res.append(array[k])
                        res.append(array[i])
                    else:
                        if array[k]*array[i]<res[0]*res[1]:
                            res=[array[k],array[i]]
            k+=1
        return res
    
'''
既然是有序的，和相等，要求乘积最小，那么，数值相差越大乘积越小
则，可以再头尾设两个指针i<j往中间靠近，一旦发现两个数和达到要求，直接返回这两个数
若array[i]+array[j]大于tsum，说明array[j]过大，j应该减小，
若array[i]+array[j]小于tsum，说明array[i]过小，i应该减大
'''