from math import *
func = input()
A, B = eval(input())
x = A
while abs(eval(func)) > 0.0000001:
    x = (A + B) / 2
    if eval(func) < 0:
        A = x
    else:
        B = x
print(x)
