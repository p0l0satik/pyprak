num = int(input())
Sum, maxSum = 0, num

while num:
    if maxSum < 0:
        if num < 0 and maxSum < num:
            maxSum = num
        if num > 0:
            Sum = maxSum = num
    else:
        if num > 0:
            Sum += num
        else:
            if Sum + num > 0:
                Sum += num
            else:
                Sum = 0   
        if Sum > maxSum:
            maxSum = Sum
        
    num = int(input())
print(maxSum)

    