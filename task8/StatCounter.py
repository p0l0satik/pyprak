def statcounter():
    dict = {}
    func = yield dict

    while True:
        dict.setdefault(func, 0)
        def wrapper(*args, fun = func):
            dict[fun] += 1
            return fun(*args)
        func = yield wrapper

