t, n = input().split(" ")
lst = [[int(x) for x in input().split(" ")] for y in range(int(t))]
p = [x[1] for x in lst]
maxi = 0
for i in range(int(t)-(int(t) % int(n))):
    if maxi < sum(p[i:i+int(n)]):
        maxi = sum(p[i:i+int(n)])
        index = i
print(lst[index][0])
