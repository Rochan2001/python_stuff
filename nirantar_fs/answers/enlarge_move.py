import pandas as pd
r = int(input())
c = int(input())
m = [[int(i) for i in input().split()] for i in range(r)]
matrix = pd.DataFrame(m)
for i in range(r):
    max_ = max(m[i])
    for j in range(c):
        min = matrix[j].min()
        m[i][j] = m[i][j]+max_+min
for i in range(r):
    for j in range(c):
        print(m[i][j],"",end='')
    print("")