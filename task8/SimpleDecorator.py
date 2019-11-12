def nonify(func):
    def newAnB(*args, **arg):
        res = func(*args, **arg)
        return None if not res else res
    return newAnB

