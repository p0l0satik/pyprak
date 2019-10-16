M, N = eval(input())
#n strok
n, m = 0, 0
d = 0
pos = 0
i = N * M
a = [[-1] * M for i in range(N)]
while i:
    a[n][m] = pos
    pos = (pos + 1) % 10
    i -= 1
    if d == 0 and (m + 1 >= M or a[n][m + 1] != -1):
        d = 1
    elif d == 1 and (n + 1 >= N or a[n + 1][m] != -1):
        d = 2
    elif d == 2 and (m - 1 == -1 or a[n][m - 1] != -1):
        d = 3
    elif d == 3 and (n - 1 == -1 or a[n - 1][m] != -1):
        d = 0

    if d == 0:
        m += 1
    if d == 1:
        n += 1
    if d == 2:
        m -= 1
    if d == 3:
        n -= 1

for i in a:
    print(*i)

    
    


