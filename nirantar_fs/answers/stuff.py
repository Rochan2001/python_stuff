n = int(input())
words = []
for i in range(n):
    words.append(input())
w = input()
s = 0
d = {}
for i in words:
    s = 0
    for j in range(len(i)):  
        for k in range(len(w)):
            if i[j] == w[k]:
                s+=((j+1)*(k+1))
    d[i]=s
v = list(d.values())
k = sorted(list(d.keys()))
m = max(v)
for i in k:
    if d[i] == m:
        print(i)

    
