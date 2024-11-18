import random

class Matrix:
    def __init__(self, rows, cols, matrix=None):
        self.rows = rows
        self.cols = cols
        if matrix is None:
            self.matrix = [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]
        else:
            self.matrix = matrix
        
    def __str__(self):
        result = ""
        for row in self.matrix:
            for value in row:
                result += str(value) + " "
            result = result.strip() + "\n"
        return result.strip()

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions.")
        
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)]for i in range(self.rows)]
        return Matrix(self.rows, self.cols, result)
    
    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions.")
        
        result = [[self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)]for i in range(self.rows)]
        return Matrix(self.rows, self.cols, result)
    
    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns of the first matrix must be equal to the number of rows of the second matrix.")
        
        result = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.cols)) for j in range(other.cols)]for i in range(self.rows)]
        return Matrix(self.rows, other.cols, result)

def main():

    matrix1 = Matrix(3, 3)
    matrix2 = Matrix(3, 3)
    
    print("Matrix 1:")
    print(matrix1)
    
    print("\nMatrix 2:")
    print(matrix2)
    
    print("\nMatrix 1 + Matrix 2:")
    print(matrix1 + matrix2)
    
    print("\nMatrix 1 - Matrix 2:")
    print(matrix1 - matrix2)
    
    print("\nMatrix 1 * Matrix 2:")
    print(matrix1 * matrix2)

if __name__ == "__main__":
    main()
