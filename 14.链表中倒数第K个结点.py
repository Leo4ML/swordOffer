# -*- coding:utf-8 -*-

class Solution:
    def FindKthToTail(self, head, k):
        l=[]
        n=0
        while head!=None:
            n+=1
            l.append(head)
            head=head.next
        if n-k+1<=0 or k==0:
            return None
        else:
            return l[-k]