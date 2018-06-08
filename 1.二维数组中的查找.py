# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 20:55:35 2018

@author: Leo
"""

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        new=[]
        for i in range(len(array)):
            if target in array[i]:
                new.append('True')
        if 'True' in new:
            return True
        else:
            return False

target=5
array=[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
s=Solution()
print s.Find(target,array)

'''

            '''