print('{0:-^30}'.format('print read'))
#print函数会在结尾自动加入换行
with open('print.format.py') as song:
    print(song.read(1))
    print(song.read(8))
    print(song.read(8))
    #print(song.read())

print('{0:-^30}'.format('print read end none'))
with open('print.format.py') as song:
    print(song.read(1), end = '')
    print(song.read(8), end = '')
    print(song.read(8))
    #print(song.read())

print('{0:-^30}'.format('print readline'))
with open('print.format.py') as song:
    print(song.readline())
    print(song.readline())
    print(song.readline(1), end = '\n\n')
    #可以看出readlline()是每次读取一行（/n换行跟随上一行，不会算成下一行）
    #如果readline(x),就是读出这行的x个字符
    #这种方式时结尾的/n不会打印
    #结尾\n\n 才会换行，一个的话会追加到x个字符后面

print('{0:-^30}'.format('print readlines'))
with open('print.format.py') as song:
    print(song.readlines(), end = '\n\n')
    #readlines是把所有行读入到一个列表中

print('{0:-^30}'.format('for line in file'))
test_lines = []
with open('print.format.py') as song:
#line可以替换成i，只不过line比较明确
#这里重点是，对于open的文件，for 循环是每次循环一行
    for line in song:
        test_lines.append(line.strip())
    print(test_lines,end = '\n\n')

print('{0:-^30}'.format('split lines'))
def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    with open("circus.csv") as f:
        for line in f:
            name=line.split(',')[0]
            cast_list.append(name.strip())
        #下面的是最后一个循环的输出，输出做对比就明白很多了：
        print('{0:-^30}'.format('under is split testing'))
        print('originial: {0:#^20}'.format(line), end = '')
        nameall = line.split(',')
        nameallfirst = line.split(',')[0]
        print(name)
        print(nameall)
        print(nameallfirst)
    #use the for loop syntax to process each line
    #and add the actor name to cast_list

    return cast_list

cast_list = create_cast_list('circus.csv')
for actor in cast_list:
    print(actor)
