def max_cost(choco,brand,no_choco,b_limit):
    b_count = dict()
    m = 0
    c = 0
    i = 0
    while(c<no_choco and i<len(choco)):
        b_count[brand[i]] = b_count.get(brand[i],0)
        if b_count[brand[i]] < b_limit:
            m+=choco[i]
            b_count[brand[i]] = b_count.get(brand[i],0)+1
            c+=1
        i+=1
    return m
n = int(input())
choco = []
brand = []
for i in range(n):
    choco.append(int(input()))
for j in range(n):
    brand.append(int(input()))
no_choco = int(input())
b_limit = int(input())
print(max_cost(choco, brand,no_choco,b_limit))
