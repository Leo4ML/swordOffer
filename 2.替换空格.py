# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 20:10:54 2018

@author: Leo
"""
strr=raw_input()
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        '''
        sl = s.split()
        if s[0]!=' ' and s[-1]!=' ':   #这四个if没有考虑到连续的空格应该被替换为连续的%20而不是一个%20
            #sl = s.split()
            return '%20'.join(sl)
        if s[0]!=' ' and s[-1]==' ':
            #sl = s.split()
            return '%20'.join(sl)+'%20'
        if s[0]==' ' and s[-1]!=' ':
            #sl = s.split()
            return '%20'+ '%20'.join(sl)
        if s[0]==' ' and s[-1]==' ':
            return '%20'+ '%20'.join(sl)+'%20'
            '''
        s=list(s)
        for i in range(len(s)):          #这里list（）函数可以把字符串中所有的元素都能保留到列表中，从而直接替换
            if s[i]==' ':
                s[i]='%20'
        return ''.join(s)
    '''
        s=s.replace(' ','%20')
        return s                      #巧用replace() 也是可行的
    '''
    
s=Solution()
print s.replaceSpace(strr)