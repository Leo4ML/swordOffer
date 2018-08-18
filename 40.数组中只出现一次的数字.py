def FindNumsAppearOnce(array):
    # write code here
    temp=0
    for i in range(len(array)-1):
        temp^=i
    idx=0
    while temp & 1 ==0:
        temp>>=1
        idx+=1
    a=0
    b=0
    for i in array:
        if self.isbit(i,idx):
            a^=i
        else:
            b^=i
    return [a,b]
def isbit(i,idx):
    if i>>idx & 1 ==0:
        return False
    
'''
通过新数组，来筛选
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        L=[]
        res=[]
        i=0
        for i in range(len(array)):
            if array[i] not in L:
                L.append(array[i])
                array[i]='-1'
            if array[i] in L:
                continue

        for x in range(len(L)):
            if L[x] not in array:
                res.append(L[x])
        return res
'''