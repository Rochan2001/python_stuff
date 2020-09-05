n = int(input())
c = sorted([[int(x) for x in input().split()] for y in range(n)])
max_dist = 0
for i in range(n):
  for j in range(i+1, n):
    if c[i][0] == c[j][0]:
      dist = abs(c[i][1]-c[j][1])
      if dist > max_dist:
        max_dist = dist
        pos1 = i
        pos2 = j
        p = (j+1) - i
print(c[pos1][0], c[pos1][1])
print(c[pos2][0], c[pos2][1])
print(max_dist)
print(p)
