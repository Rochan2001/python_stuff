s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s1 = input()
s2 = input()
s3 = ""
for i in range(3):
    a = abs(s.find(s1[i])-s.find(s2[i]))
    b = s.find(s2[i])
    if a+b > 25:
        temp1 = s[26-(a+b)]
    else:
        temp1 = s[abs(s.find(s1[i])-s.find(s2[i]))+s.find(s2[i])]
    s3 += temp1
print(s3)
