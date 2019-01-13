tabledata = [['apples','oranges','cherries','banana'],\
['Alice','Bob','Carol','David'],\
['dogs','cats','moose','goose']]

colwidth = [0]*len(tabledata)

def ptable(tabledata):
	#colwidth = [0]*len(tabledata)
	#issue this line will make colwidth reset,why?
	#out of def, will not?
	i = len(tabledata)-1
	while i >= 0:
		ii = len(tabledata[i])-1
		n = 0
		while ii >= 0:
			if len(tabledata[i][ii]) > n:
				n = len(tabledata[i][ii])
			else:
				pass
			ii = ii-1
		colwidth[i] = n
		#print('colwidth',colwidth[i])
		i = i-1
		#print(colwidth)
ptable(tabledata)
print(colwidth)

def showitem1():
	i = 0
	while i <= len(tabledata):
		print(tabledata[0][i].rjust(colwidth[0]) + ' ' + tabledata[1][i].ljust(colwidth[1]+1) + tabledata[2][i].ljust(colwidth[2]))
		i = i+1
showitem1()

#本想写一个遍历n*m列的阵列，但是很别扭。感觉不是这样实现，drop

