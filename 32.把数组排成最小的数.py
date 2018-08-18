# -*- coding: utf-8 -*-

def MiniNumber(arr):
    if numbers==[]:
        return ''
    res=''
    while len(arr)!=1:
        indexx=0
        for x in range(len(arr)):
            if x==indexx:
                continue
            if int(str(arr[indexx])+str(arr[x]))>int(str(arr[x])+str(arr[indexx])):
                indexx=x
        res+=str(arr[indexx])
        del arr[indexx]
    res+=str(arr[0])
    return int(res)