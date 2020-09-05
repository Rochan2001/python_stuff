x, y = [int(a) for a in input().split()]
d = dict()
list1=[]
for i in range(x):
    key, value = [a for a in input().split()]
    d[key] = value
z = sorted(d.items())
print(z)

for key1, value1 in sorted(z, key=lambda kv: kv[1], reverse=True):
    list1.append(key1)
for i in range(y):
    print(list1[i])
