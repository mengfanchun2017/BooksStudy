def power(x,y):
    if y == 0:
        return 2
    else:
        return x*power(x,y-1)

print(power(2,3))