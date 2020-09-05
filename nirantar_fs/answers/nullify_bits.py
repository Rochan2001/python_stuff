n = int(input())
binary = list(bin(n).replace("0b", ""))
binary = binary[::-1]
odd_bit = 0
even_bit = 0
e = []
o = []
for index, i in enumerate(binary):
    if i == '1' and index % 2 == 0:
        odd_bit += 1
        o.append(index)

    if i == '1' and index % 2 == 1:
        even_bit += 1
        e.append(index)
if odd_bit < even_bit:
    for index, i in enumerate(binary):
        if index in o:
            binary[index] = '0'
else:
     for index, i in enumerate(binary):
        if index in e:
            binary[index] = '0'

t = "".join(binary[::-1])
print(int(t, 2))
