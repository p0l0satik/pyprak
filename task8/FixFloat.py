def fix(n):
    def dec(func):
        def wrapper(*args, **kwargs):
            res = func(*[round(i, n) for i in args], **{el[0]: round(el[1], n) for el in kwargs.items()})
            return round(res, n)
        return wrapper
    return dec
