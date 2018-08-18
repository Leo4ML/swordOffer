# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        res=0
        for i in data:
            if i==k:
                res+=1
            if i >k:
                break
        return res
    
'''
看到有序第一反应应该是二分查找
def GetNumberOfK(data, k):
    # write code here
    start=0
    end=len(data)-1
    while start<=end:
        mid=start+(end-start)/2
        if data[mid]<k:
            start=mid+1
        if data[mid]>k:
            end=mid-1
        if data[mid]==k:
            res=1
            while (mid-1)>=0 and data[mid-1]==k:
                res+=1
                mid=mid-1
            mid=mid+res-1
            while (mid+1)<len(data) and data[mid+1]==k:
                res+=1
                mid+=1
            return res
    return 0
'''