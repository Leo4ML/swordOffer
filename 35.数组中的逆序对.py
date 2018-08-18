
#def InversePairs(data):
#    # write code here
data=[364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]

big=[]
small=[]
res=[]
cur=0
for i in range(len(data)):
    if data[i]<data[cur]:
        small.append(data[i])
    else:
        big.append(data[i])
res.append(len(small))
del big[0]
while len(res)!=len(data)-1:
    cur+=1
    if data[cur]>data[cur-1]:
        del big[0]
        if big==[]:
            res.append(0)
        else:
            x=0
            while x<len(big):
                if big[x]<data[cur]:
                    small.append(big[x])
                    del big[x]
                else:
                    x+=1
            res.append(len(small))
    if data[cur]<data[cur-1]:
        del small[0]
        if small==[]:
            res.append(0)
        else:
            y=0
            while y < len(small):
                if small[y]>=data[cur]:
                    big.append(small[y])
                    del small[y]
                else:
                    y+=1
            res.append(len(small))
    if data[cur]==data[cur-1]:
        del big[0]
        res.append(len(small))
print sum(res)%1000000007

