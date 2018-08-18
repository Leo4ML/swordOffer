# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        res=1
        if not pRoot:
            return 0
        if pRoot.left==None and pRoot.right==None:
            return res
        return res+max(self.TreeDepth(pRoot.left),self.TreeDepth(pRoot.right))