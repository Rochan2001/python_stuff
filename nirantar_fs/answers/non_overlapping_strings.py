s = input()
n = int(input())
c = 0
temp = 0
for i in set(s):
    temp = 0
    for j in s:
        if i == j:
            temp += 1
    st = s[s.index(i):s.index(i)+temp]
    if st.count(st[0]) >= n:
        c += 1
print(c)
