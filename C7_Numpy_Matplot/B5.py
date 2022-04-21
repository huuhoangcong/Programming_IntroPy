import numpy as np


class SquareMatrix:

    def __init__(self,M):
        self.M = M
        self.A = np.random.randint(low = -100, high = 101, size = (M,M))

    def getPositive_Negative(self):
        pos = np.argwhere(self.A>0)
        P = []
        N = []
        for i in range(len(pos)):
            P.append(self.A[pos[i][0]][pos[i][1]])
        
        for i in self.A:
            for j in i:
                if j!=0 and j not in P:
                    N.append(j)

        U = P + N

        return "Positive: {0}\nNegative: {1}\nUnequal Zero: {2}".format(P,N,U)

    def sumAll(self):
        return f"Sum of all Element is: {np.sum(self.A)}"

    def sumRows(self):
        S = [sum(i) for i in self.A]
        text = ""
        for i in range(len(S)):
            text += f"Sum of row {i+1} is: {S[i]}\n"

        return text

    def sumColumns(self):
        rows = [i for i in self.A]
        listS = []
        for j in range(len(rows[0])):
            s = 0
            for i in range(len(rows)):
                s += rows[i][j]
            listS.append(s)

        text = ""
        for i in range(len(listS)):
            text += f"Sum of column {i+1} is: {listS[i]}\n"

        return text

    def cumulative_Sum_Product(self,n):
        if n > self.M:
            return f"{n} is out of size of Matrix"
        else:
            #Cumulative sum and product of each Column 
            a = np.cumsum(self.A, axis = 0)
            c = np.cumprod(self.A, axis = 0)

            #Cumulative sum and product of each Column 
            b = np.cumsum(self.A, axis = 1)
            d = np.cumprod(self.A, axis = 1)

            S = [b[n-1][len(self.A[0])-1], a[len(self.A)-1][n-1]]
            P = [d[n-1][len(self.A[0])-1], c[len(self.A)-1][n-1]]

            return f"Cumulative Sum of Row {n} is: {S[0]}\nCumulative Sum of Column {n} is: {S[1]}\nCumulative Product of Row {n} is: {P[0]}\nCumulative Product of Column {n} is: {P[1]}"

    def sumofNegative(self):
        return np.sum(self.A) - self.sumofPositive() 
    
    def sumofPositive(self):
        pos = np.argwhere(self.A>0)
        P = []
        for i in range(len(pos)):
            P.append(self.A[pos[i][0]][pos[i][1]])
        
        return sum(P)

    def sortRow(self, n):
        if n > self.M:
            return f"{n} is out of size of Matrix"
        else:
            indices = np.argsort(self.A, axis = 1)[n-1]
            result = []
            for i in range(len(self.A)):
                result.append(np.take_along_axis(self.A[i], indices, axis = 0))

            return np.array(result)

    def changeByX(self, X):
        cop = np.copy(self.A)
        for i in range(len(self.A)):
            for j in range(len(self.A[0])):
                if self.A[i][j] > X:
                    cop[i][j] = 1
                elif self.A[i][j] < X:
                    cop[i][j] = 0

        return cop

    def changeByMultiple(self, X):
        cop = np.copy(self.A)
        for i in range(len(cop)):
            for j in range(len(cop[0])):
                if cop[i][j] % X == 0:
                    cop[i][j] = X
        
        return cop

    def devide_EvenNumber_By2(self):
        cop = np.copy(self.A)
        for i in range(len(cop)):
            for j in range(len(cop[0])):
                if cop[i][j] % 2 == 0:
                    cop[i][j] = cop[i][j]/2 
        
        return cop

    def mul_OddNumber_Byitself(self):
        cop = np.copy(self.A)
        for i in range(len(cop)):
            for j in range(len(cop[0])):
                if cop[i][j] % 2 != 0:
                    cop[i][j] = cop[i][j]**2 
        
        return cop

    def changeElement_lessThan_averageOfMatrix(self):
        a = np.sum(self.A)/2
        cop = np.copy(self.A)
        for i in range(len(cop)):
            for j in range(len(cop[0])):
                if cop[i][j] < a:
                    cop[i][j] = 0 
        
        return cop
            






M = int(input("Kich thuoc ma tran M = "))
A = SquareMatrix(M)

print(A.A)
print(A.getPositive_Negative())
print(A.sumAll())
print(A.sumRows())
print(A.sumColumns())
print(A.cumulative_Sum_Product(int(input("Nhap n: "))))
print(A.sumofPositive())
print(A.sumofNegative())
print(A.sortRow(2))
print(A.changeByX(4))
print(A.changeByMultiple(3))
print(A.devide_EvenNumber_By2())
print(A.mul_OddNumber_Byitself())
print(A.changeElement_lessThan_averageOfMatrix())