num = int(input())
num_s = num
per = 0
i = 1
while num:
    per *= 10
    per += (num % 10)
    num //= 10
if num_s == per:
    print("YES")
else:
    print ("NO")

