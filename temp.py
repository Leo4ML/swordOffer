# -*- coding:utf-8 -*-

       # write code here
L=[]
c=0
a=[1,2,3,4,5]
b=[4,5,3,2,1]
for i in a:
    if i !=b[c]:
        L.append(i)
    else:
        c+=1
                
if b[c:-1]==L[::-1]:
    print (True)
else:
    print (False)
        

