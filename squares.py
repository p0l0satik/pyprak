a, b = input(), input()
num = 0
while b[0] != "-":
    a = b
    b = input()
    for i, el in enumerate(a):
        if el == "#" and (i + 1 == len(a) or (a[i + 1] != "#" and b[i + 1] != "#")) and b[i] != "#":
            num += 1
print(num)