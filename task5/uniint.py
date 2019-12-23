arr = eval(input())
cords = []
for el in arr:
    cords.append((el[0], "l"))
    cords.append((el[1], "r"))
cords.sort()
# print(cords)
c, res  = 0, 0
for i, el in enumerate(cords):
    if (c and i):
        res += el[0] - cords[i - 1][0]
    if el[1] == "r":
        c += 1
    else:
        c -= 1
print(res)