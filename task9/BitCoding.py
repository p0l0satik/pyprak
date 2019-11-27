from collections import Counter
def xehs(s):
    tmp = []
    for c in s:
        tmp.append(bin(ord(c) - 32)[2:])
    return int("".join(tmp), 2)

def shex(n):
    s = []
    some = bin(n)


    some = ((6 - (len(some)-2) % 6) % 6) * "0" + some[2:]

    for i in range(0, len(some), 6):
        s.append(chr(int(some[i: i + 6], 2) + 32))
    
    return "".join(s)

def cmp(c):
    a, b = c[0], c[1]

    if a[1] == b[1]:
        return a if a[0] < b[0] else b
    else:
        return a if a[1] > b[1] else b

def encode(txt):
    num = []
    srt = sorted(Counter(txt).items(), key = cmp)
    enc = {b[0] : "1" * (a - 1) + "0"  for a, b in enumerate(srt)}
    
    for i in txt:
        num.append(enc[i])
    return (len(txt), "".join(dict(srt).keys()), shex(int("".join(num))))





