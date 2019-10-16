def maxfun(l, *arr):
    maxn = 0
    maxsum = 0
    for k, i in enumerate(arr):
        s = 0
        for t in l:
            s += i(t)
        if s >= maxsum:
            maxn = k
            maxsum = s
    return arr[maxn]
