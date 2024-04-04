def sum_digits(num):
    res = 0
    while num > 0:
        res += num % 10
        num = num // 10
    return res
    
x = int(input())
while x != 0:
    sum_x = sum_digits(x)
    i = 11
    while i < 100000:
        sum_y = sum_digits(x*i)
        if sum_y == sum_x:
            print(i)
            break
        i += 1
    x = int(input())