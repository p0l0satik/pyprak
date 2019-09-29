num = int(input())
i = 2
while i <= 50000:
    j = 2
    fl = False
    while i ** j <= num:
        if (i ** j == num):
            print("YES")
            fl = True
            break;
        j += 1
    i += 1
    if fl:
        break
else:
    print("NO")
