class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        L=[]
        # write code here
        if root==None:
            return None
        else:
            L.append(root)
        while L!=[]:
            head=L.pop(0)
            print (head.val)
            if head.left!=None:
                L.append(head.left)
            if head.right!=None:
                L.append(head.right)
        

