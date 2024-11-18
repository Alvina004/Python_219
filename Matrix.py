import random
class myMatrix:
    def __init__(self, m, n):
        """Initialize the matrix with n rows and m columns"""
        self.m=m
        self.n=n
        self.matrix=[[random.randint(1,100) for _ in range(m)]for _ in range(n)]
    
    def printMatrix(self):
        """Prints matrix:"""
        for row in self.matrix:
            for value in row:
                print(value, end= " ")
            print()
            
    def mean(self):
        """Calculates the mean of the matrix"""
        total=0
        count=self.m * self.n
        for row in self.matrix:
            for value in row:
                total+=value
        return total/count
    def sumOfRow(self, row):
        """Calculates the sum of a given row"""
        try:
            total=0
            for value in self.matrix[row]:
                total+=value
            return total
        except IndexError:
            raise ValueError("Row index out of bounds.")
            
    def averageOfCol(self, col):
        """Calculates the average of a given column"""
        try:
            total=0
            for i in range(self.n):
                total+=self.matrix[i][col]
            return total/self.n
        except IndexError:
            raise ValueError("Column index out of bounds.")
     
    def printSubMatrix(self, row1, row2, col1, col2):
        """Prints the submatrix"""
        if row1 < 0 or row2 >= self.n or col1 < 0 or col2 >= self.m:    
            raise ValueError("Indices out of bounds ")
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                print(self.matrix[i][j], end=" ")
            print()
            
if __name__== "__main__":
    matrix= myMatrix(5,4)
    print("Matrix: ")
    matrix.printMatrix()

    print("\nMean of matrix:", matrix.mean())
    print("Sum of row 2:", matrix.sumOfRow(2))
    print("Average of column 1:", matrix.averageOfCol(1))
        
    print("\nSubmatrix from [0, 2, 1, 3]:")
    matrix.printSubMatrix(0, 2, 1, 3)
