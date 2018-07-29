# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self, node):
        # write code here
        if self.stack1==[]:
            self.stack1.append(node)
            self.stack2.append(node)
        else:
            self.stack1.append(node)
            if self.stack2[-1]<=node:
                self.stack2.append(self.stack2[-1])
            else:
                self.stack2.append(node)
    def pop(self):
        # write code here
        if self.stack1==[]:
            return None
        else:
            del self.stack2[-1]
            return self.stack1.pop()
    def top(self):
        # write code here
        if self.stack1==[]:
            return None
        else:
            return self.stack1[-1]
    def min(self):
        # write code here
        if self.stack2!=[]:
            return self.stack2[-1]
        