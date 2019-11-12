d = {}
nvis = set()
s = input()

while " " in s:
    k, v = s.split()
    if k == v:
        continue
    nvis.add(k)
    nvis.add(v)
    d.setdefault(v, [])
    d.setdefault(k, [])
    if v not in d[k]:
        d[k].append(v)
    if k not in d[v]:
        d[v].append(k)
    s = input()
now = [s,]
out = input()
while len(now) and len(s):
    proc = now.pop()
    if proc == out:
        print("YES")
        break
    if proc in nvis:
        nvis.remove(proc)
        for t in d[proc]:
            if t in nvis:
                now.append(t)
else:
    print("NO")



