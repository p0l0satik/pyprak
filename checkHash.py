def checkhash(seq, f, mod):
    repeat = {}
    for el in seq:
        res = f(el) % mod
        repeat.setdefault(res, 0)
        repeat[res] += 1
    return (max(repeat.values()), min(repeat.values()))
