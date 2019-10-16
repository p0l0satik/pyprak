a = eval(input())
l = list()
for el in a:
    if type(el) is int:
        if el > len(l):
            break
        else:
            print(tuple(l[0:el]))
            del(l[0:el]) 
    else:
        for g in el:
            l.append(g)
