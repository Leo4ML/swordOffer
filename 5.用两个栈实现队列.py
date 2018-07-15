# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 17:05:01 2018

@author: Leo
"""

class Solution:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self, node):
        self.stack1.append(node)
        # write code here
    def pop(self):
        if self.stack2==[]:
            while self.stack1!=[]:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()