num = {1,2,3,4,5,6}
num = {0,1,2,3} & num
print(num)
num = filter(lambda x:x>1, num)
print(len(list(num)))