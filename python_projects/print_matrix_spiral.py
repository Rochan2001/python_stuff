class Spiral:
    def __init__(self, matrix):
        self.matrix = matrix

    def print_spiral(self, i, j, r, c):
        # If i or j lies outside the matrix
        if i >= r or j >= c:
            return
        # Print First Row
        for index in range(i, c):
            print(self.matrix[i][index], end=" ")
        #Print Last Column
        for index in range(i+1, r):
            print(self.matrix[index][c-1], end=" ")
        # Print Last Row, if Last and
        # First Row are not same
        if ((i-1) != r):
            for index in range(c-1, i, -1):
                print(self.matrix[c-1][index-1], end=" ")
        #Print First Column, if Last and
        #First Column are not same
        if ((j-1) != c):
            for index in range(r-1, j+1, -1):
                print(self.matrix[index-1][j], end=" ")
        return Spiral.print_spiral(self, i+1, j+1, r-1, c-1)

print("Enter the dimensions of a square matrix(m x n) :")
r,c = list(map(int,input().split()))
try:
    if r == c:
        matrix = [[int(x) for x in input().split()] for i in range(c)]
        s_matrix = Spiral(matrix)
        s_matrix.print_spiral(0,0,r,c)
    else:
        raise Exception("Dimensions do not match!")
except Exception as e:
    print(e)

