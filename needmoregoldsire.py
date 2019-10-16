def moar(a, b, n):
    return len(list(i for i in a if i % n == 0)) > len(list(i for i in b if i % n == 0))