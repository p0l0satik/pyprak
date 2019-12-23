s = input()
shs = input()
store = -1
i, sub = 0, 0
arr = shs.lstrip("@").split("@")
# print(arr)
while i < len(shs) and shs[i] == "@":
    sub += 1
    i += 1
while 1:
    pos = s.find(arr[0], i)
    if pos != -1:
        for k, j in enumerate(shs):
            if j == "@":
                continue
            elif s[k + pos - sub] != j:
                i = k + pos
                break
        else:
            print(pos - sub)
            break
    else:
        print(-1)
        break 


        
