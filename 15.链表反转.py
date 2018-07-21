# -*- coding: utf-8 -*-

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        
        if not pHead or not pHead.next:
            return pHead
        pre=None
        now=pHead
        nex=now.next
        while nex!=None:
            now.next=pre
            pre=now
            now=nex
            nex=nex.next
        now.next=pre
        pre=now
        now=nex
        return pre
    
    
#在python 最好用第8 9行的代码去说名为空而不是用pHead==None这种形式