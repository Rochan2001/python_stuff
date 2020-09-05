r = int(input())
c = int(input())
m = [[int(i) for i in input().split()] for i in range(r)]
# max1 = m[0][0]+m[0][1]+m[1][0]+m[1][1]
# max_pos = []
# max_value = []
# max_value.append(max1)
max1=-999
for i in range(r-1):
    for j in range(c-1):
        #max1 = max(max_value)
        # if i < r-1 and j < c-1:
        #     if i !=0 or j != 0:
        if m[i][j]+m[i][j+1]+m[i+1][j]+m[i+1][j+1] >= max1:
            max1=m[i][j]+m[i][j+1]+m[i+1][j]+m[i+1][j+1]
            # if m[i][j]+m[i][j+1]+m[i+1][j]+m[i+1][j+1] > x:
            #             max_pos.clear()
            #             max_value.clear()
            #         max_value.append(m[i][j]+m[i][j+1]+m[i+1][j]+m[i+1][j+1])
            #         max_pos.append((i,j))
            #         max1 = m[i][j]+m[i][j+1]+m[i+1][j]+m[i+1][j+1] 
print(max1)
for i in range(r-1):
    for j in range(c-1):
        if m[i][j]+m[i][j+1]+m[i+1][j]+m[i+1][j+1] == max1:
            print(i+1,j+1,end=" ")
            print()
            print(m[i][j],m[i][j+1],m[i+1][j],m[i+1][j+1],end=" ")
            print()
            
# for i in range(len(max_pos)):
#     print(max_pos[i][0]+1,max_pos[i][1]+1,end=" ")
#     print()
#     print(m[max_pos[i][0]][max_pos[i][1]],m[max_pos[i][0]][max_pos[i][1]+1],m[max_pos[i][0]+1][max_pos[i][1]],m[max_pos[i][0]+1][max_pos[i][1]+1],end=" ")
#     print()




