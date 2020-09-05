a = input()
count = 0

if len(a) % 2 == 0:
    for i in range(1, len(a) + 1):
        if a[i - 1] == 'A' or a[i - 1] == 'B':
            y = a.count(('A' * i + 'B' * i))
            x = a.count(('B' * i + 'A' * i))
            z = x + y
            count = count + z
        else:
            count = -1
            break
    print(count)
