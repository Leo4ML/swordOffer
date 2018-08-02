class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        res=[]
        L=[]
        for a in numbers:
            if a not in L:
                L.append(a)
        for i in L:
            c=0
            for x in numbers:
                if i==x:
                    c+=1
            res.append(c)
        for y in range(len(res)):
            if res[y]>len(numbers)/2:
                return numbers[y]
        return 0