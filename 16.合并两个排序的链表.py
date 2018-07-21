
#非递归法1：这是利用了一个数组排好序后，重建链表做法
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        L=[]
        if (not pHead1) and (not pHead2):
            return pHead1
        while pHead1!=None and pHead2!=None:
            if pHead1.val<=pHead2.val:
                L.append(pHead1)
                pHead1=pHead1.next
            else:
                L.append(pHead2)
                pHead2=pHead2.next
        while pHead2!=None and pHead1==None:
            L.append(pHead2)
            pHead2=pHead2.next
        while pHead1!=None and pHead2==None:
            L.append(pHead1)
            pHead1=pHead1.next
        if pHead1==None and pHead2==None:
            for i in range(len(L)-1):
                L[i].next=L[i+1]
            L[-1].next=None
        return L[0]# -*- coding: utf-8 -*-

'''
#非递归法2：新建链表。然后依次比对大小加入新链表中
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here

        res=node=ListNode(0)
        while pHead1!=None and pHead2!=None:
            if pHead1.val<=pHead2.val:
                node.next=pHead1
                pHead1=pHead1.next
            else:
                node.next=pHead2
                pHead2=pHead2.next
            node=node.next
#其实第46-49行用一句node.next=pHead1 or pHead2 即可
        if not pHead1 and not pHead2:
            return pHead1
        else:
            node.next=pHead1 or pHead2
        return res.next
'''
'''
#递归方法：
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        node=None
        if pHead1.val<=pHead2.val:
            node=pHead1
            node.next=self.Merge(pHead1.next,pHead2)
        else:
            node=pHead2
            node.next=self.Merge(pHead1,pHead2.next)
        return node
'''
