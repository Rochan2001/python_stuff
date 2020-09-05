lst = []
r = int(input())
c = int(input())
col = []
for i in range(r):
    a = input().split()
    col.append(a)
    if 'l' in a and 'l' not in lst:
        lst.append('l')
    if 'z' in a and 'z' not in lst:
        lst.append('z')
    if 'x' in a and 'x' not in lst:
        lst.append('l')

if(len(lst) != 3):
    print("Invalid")
else:
    count1 = 0
    for i in range(r-1):
        for j in range(c-1):
            if(col[i][j] == 'l' and col[i+1][j] == 'l' and col[i+1][j+1] == 'l'):
                count1 += 1
    print(count1)
