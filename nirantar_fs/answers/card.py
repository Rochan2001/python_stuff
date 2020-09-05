n = int(input())
find = int(input())
lst = []
nums = []
temp = 0
for i in range(n, (n*n)+1, n):
    if (temp % 2 == 0):
        for j in range(i-n, i):
            lst.append(j+1)
    elif temp % 2 == 1:
        for k in range(i-1, i-n, -1):
            lst.append(k)
        lst.append(i)
    nums.extend(lst)
    temp += 1
    lst.clear()
x = (nums.index(find)+1) % n
if x == 0:
    print("S"+str(n))
else:
    for i in range(1, n+1):
        if x == i:
            print("S"+str(i))
