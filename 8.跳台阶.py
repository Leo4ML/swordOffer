# -*- coding:utf-8 -*-

class Solution:
    def jumpFloor(self, number):
        # write code here
        s=[0,1,2,3]
        a=3
        if number<=3:
            return number
        while a<number:
            s.append(s[a-1]+s[a])
            a=a+1
        return s[number]
'''
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number<=2:
            return number
        else:
            x=Solution()
            return x.jumpFloor(number-1)+x.jumpFloor(number-2)
x=Solution()
print x.jumpFloor(5)
#不懂为何第二种做法牛客网无法通过
'''