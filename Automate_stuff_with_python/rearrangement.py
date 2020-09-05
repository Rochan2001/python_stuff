n = [int(x) for x in input().split()]
list = []
for i in range(max(n)+1):
  list.append(str(i)) if i in n else list.append('-1')
print(' '.join(list), end="")
