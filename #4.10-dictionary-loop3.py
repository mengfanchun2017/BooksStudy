import random
import copy
#/1/ 逗号代码
spam = ['apples', 'bananas', 'tofu', 'cats']
# 编写一个函数，它以一个列表值作为参数，返回一个字符串。
# 该字符串包含所有表项，表项之间以逗号和空格分隔，并在最后一个表项之前插入and。
##使用.index()查看序号 .开头的是方法，和函数类似，只不过是调用的前面的输出
##.index()适用于单一数据类型.remove()删除
##.append().insert(1,'item')会在1位置加上item,只能用在列表
##.sort()是排序，可以加(reverse=True)参数倒序排列
##也可以加sort的规则(key=str.lower)是按照普通字典排序
print(spam.index('tofu'))
print(spam[random.randint(0,len(spam)-1)])
###随机打印一个值
#列表可以使用in，not in做判断

##列表的 = 是链接，如果修改后面的，前面的也会修改
##如果需要复制后不修改之前的要使用copy模块
##spamnew = copy.copy(spam)
##copy.deepcopy()用于copy列表中的列表
name = 'strings'
for i in name:
    print (i)
for i in spam:
    print (i,end = '')
    
##solutions
def turn(list):
    string = ''
    for i in spam:
        string = string + i + ' '
    return string

print(turn(spam))
print(type(turn(spam)))

#/2/ 字符图网格
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
##注意在列表中，后面可以换行
##print不换行需要加end=""参数：print(x, end="")
print(len(grid))
print(len(grid[0]))
print(grid[2][1])

#调用上述grid打印出下面的‘图像’
#..OO.OO..
#.OOOOOOO.
#.OOOOOOO.
#..OOOOO..
#...OOO...
#....O....
#你需要使用循环嵌套循环，打印出grid[0][0]，然后grid[1][0]，然后grid[2][0]
#以此类推，直到grid[8][0]。这就完成第一行，所以接下来打印换行。
#然后程序将打印出grid[0][1]，然后grid[1][1]，然后grid[2][1]，以此类推。
#程序最后将打印出grid[8][5]。

def transgrid(grid):
    gridx = len(grid)
    gridy = len(grid[0])
    x = 0
    y = 0
    while y < gridy:
        while x < gridx:
            print(grid[x][y])
            x = x + 1
        y = y+1
        print(y)
        
transgrid(grid)



