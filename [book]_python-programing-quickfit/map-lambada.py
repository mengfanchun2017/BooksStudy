numbers = [
          [34, 63, 88, 71, 29],
          [90, 78, 51, 27, 45],
          [63, 37, 85, 46, 22],
          [51, 22, 34, 11, 18]
          ]
#首先numbers是一个嵌套的列表，有4个元素，每个元素（每行）又包括4个元素

averages = list(map(lambda x :sum(x)/len(x),numbers))
#此处的list是将map生成的4行平均数存为一个列表
#lambada的内容是：sum(num_list)/len(num_list)，用每个元素的加和除以每个元素内部的个数
#最后numbers是输入

print(averages)
