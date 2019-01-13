letters = ['a','b','c','d','e']
nums = [0,1,4,2,3,5]
squares = [x**2 if x % 2 == 0 else x*2 for x in nums]

#print(squares)


for i, num in enumerate(nums):
    nums[i] = num + i



print(nums)

print(squares[3])

print(list(zip(letters,squares)))

print(list(zip(letters,squares))[squares[3]])
