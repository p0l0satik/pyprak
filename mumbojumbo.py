i, s1, s2 = 0, set(""), set("")
s = input()
while s:
    if i % 2 == 0:
        s1.update(set(s))
    else:
        s2.update(set(s))
    i += 1
    s = input()
if len(s1) > len(s2):
    print("Mumbo")
else:
    print("Jumbo")

    