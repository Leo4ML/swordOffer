# -*- coding:utf-8 -*-
#枚举法
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        l=list(s)
        if s=='':
            return -1
        if l[0] not in l[1:]:
            return 0
        for i in range(1,len(l)-1):
            if l[i] not in l[:i] and l[i] not in l[i+1:]:
                return i
        if l[-1] not in l[:-1]:
            return len(l)-1
        return -1