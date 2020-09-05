n = int(input())
num = [str(bin(int(x))).replace("0b", "") for x in input().split(" ")]
c = []
for i in num:
    lst = [1 for x in i if x == '1']
    c.append(sum(lst))
print(max(c))
