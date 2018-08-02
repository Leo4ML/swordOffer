class Solution:
    def Permutation(self,ss):
        # write code here
        if len(ss)==0:
            return []
        if len(ss)==1:
            return [ss]
        else:
            L=[]
            res=[]
            for q in self.Permutation(ss[0:-1]):
                res.append(list(q))
            for i in res:
                for x in range(len(i)+1):
                    i.insert(x,ss[-1])
                    L.append(''.join(i))
                    del i[x]
            return sorted(list(set(L)))