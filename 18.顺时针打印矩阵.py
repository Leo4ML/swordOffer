class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        l=[]
        if len(matrix)>1 and len(matrix[0])>1:
            for i in range(len(matrix[0])-1):
                l.append(matrix[0][i])
            for i in range(len(matrix)-1):
                l.append(matrix[i][-1])
            for i in range(len(matrix[0])-1):
                l.append(matrix[-1][len(matrix[0])-1-i])
            for i in range(len(matrix)-1):
                l.append(matrix[len(matrix)-1-i][0])
            ma=map(lambda x:x[1:-1],matrix)
            matrix=ma[1:-1]
            
            return l+self.printMatrix(matrix)
        if len(matrix)>1 and len(matrix[0])==1:
            for i in range(len(matrix)):
                l.append(matrix[i][0])
        if len(matrix)==1 and len(matrix[0])>1:
            for i in range(len(matrix[0])):
                l.append(matrix[0][i])
        if len(matrix)==1 and len(matrix[0])==1:
            l.append(matrix[0][0])
        if len(matrix)==0 or len(matrix[0])==0 or not matrix:
            return l
        return l
s=Solution() 
m=[[1]]
print s.printMatrix(m)

'''
可以模拟魔方逆时针旋转的方法，一直做取出第一行的操作
例如 
1 2 3
4 5 6
7 8 9
输出并删除第一行后，再进行一次逆时针旋转，就变成：
6 9
5 8
4 7
继续重复上述操作即可。
Python代码如下

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = []
        while(matrix):
            result+=matrix.pop(0)
            if not matrix or not matrix[0]:
                break
            matrix = self.turn(matrix)
        return result
    def turn(self,matrix):
        num_r = len(matrix)
        num_c = len(matrix[0])
        newmat = []
        for i in range(num_c):
            newmat2 = []
            for j in range(num_r):
                newmat2.append(matrix[j][i])
            newmat.append(newmat2)
        newmat.reverse()
        return newmat
'''
'''
python 中 pop函数的运用

class Solution:
 
    def printMatrix(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            if matrix:
                res += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res
'''