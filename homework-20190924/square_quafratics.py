import math, cmath
a, b, c = eval(input())
if a != 0:
    D = b ** 2 - 4 * a * c
    if D > 0:
        print("x1 =", (-b + math.sqrt(D)) / (a * 2))
        print("x2 =", (-b - math.sqrt(D)) / (a * 2))
    if D == 0:
        print("x = ", -b / (a * 2))
    if D < 0:
        print("x1 =", (-b + cmath.sqrt(D)) / (a * 2))
        print("x2 =", (-b - cmath.sqrt(D)) / (a * 2))
if a == 0:
    if b == 0:
        if c == 0:
            print("R")
        else:
            print("No Solution")
    else:
        print("x =", -c / b)
        