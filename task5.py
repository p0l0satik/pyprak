# if it sounds like magic and looks like magic and do magic
# than magic it is
num = int(input())
l = 1

mn = (l - num * num) // (10 * num - 1)
while num * num  + 10 * num * mn != l + mn:
    l *= 10
    mn = (l - num * num) // (10 * num - 1)
if num == 1:
    print(1)
else:
    print((mn + l) * 10 + num)
