# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n==0:
            return 0
        if 1<=n<10:
            return 1
        if n>=10:
            l=len(str(n))
            if str(n)[0]=='1':
#这个返回的是最高位上1出现的次数+去掉最高位后剩下部分1出现的次数+降1位后的数字（如，156对应的1-56之间1出现的次数）
                return n-10**(l-1)+1+self.NumberOf1Between1AndN_Solution(n-10**(l-1))+self.NumberOf1Between1AndN_Solution(10**(l-1)-1)
            else:
                k=int(str(n)[0])
#最高位上1出现的次数+去掉高位后剩下位数*轮次（如，231，就是0-99,100-199，两轮）+后面部分出现1的次数（231就是，200-231）
                return 10**(l-1)+k*self.NumberOf1Between1AndN_Solution(10**(l-1)-1)+self.NumberOf1Between1AndN_Solution(n-k*10**(l-1))
            
'''
补充非递归版本，通i依次为1,10,100,1000....，来统计各位上出现1的次数
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        res=0
        i=1
        while i<=n:
            a=n/i
            b=n%i
            res+=(a+8)/10*i+(a%10==1)*(b+1)
            i*=10
        return res
'''