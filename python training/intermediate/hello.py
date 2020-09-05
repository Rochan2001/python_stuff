def move_zeros(array):
    c = sum([1 for x in array if x is 0 or x is 0.0])
    not_0 = []
    for x in array:
        if x is not 0 and x is not 0.0:
            not_0.append(x)
    return not_0+(c*[0])


x = [9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]
print(move_zeros([1, None, 2, 1, 0, False, False]))
print(move_zeros(x))

