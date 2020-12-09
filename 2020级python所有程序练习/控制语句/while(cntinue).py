x = 10
while x > 0:
    if x % 3 == 0:
        x = x-1
        continue
    print(2*x, end="  ")
    x = x-1
