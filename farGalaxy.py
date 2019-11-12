from itertools import *
def calc_dist(x):
    x1, x2, x3 = x[0][0], x[0][1], x[0][2]
    y1, y2, y3 = x[1][0], x[1][1], x[1][2]
    return (x1 - y1) ** 2 + (x2 - y2) ** 2 + (x3 - y3) ** 2

dict = []
s = input()
while s != ".":
    l = s.split()
    el = [float(coord) for coord in l[:3]]
    el.append(l[-1])
    dict.append(el)
    s = input()

co = combinations(dict, 2)
res = max( co, key = calc_dist)
print(res[0][3], res[1][3]) if res[0][3] < res[1][3] else print(res[1][3], res[0][3])
