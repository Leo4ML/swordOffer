
class Solution:
    def jumpFloorII(self, number):
        # write code here
        l=[1,1,2]
        if number <=2:
            return l[number]
        s=3
        while s<=number:
            a=0
            for i in range(s):
                a=a+l[i]
            l.append(a)
            s=s+1
        return l[number]
s=Solution()
print s.jumpFloorII(4)
'''

class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number<=2:
            return number
        else:
            return 2*self.jumpFloorII(number-1)

其实可以直接2**number
另外，在定义类下面的方法中，可以self.jumpFloorII 来递归
’‘’