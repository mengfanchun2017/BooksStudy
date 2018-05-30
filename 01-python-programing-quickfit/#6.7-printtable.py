tabledata = [['apples','oranges','cherries','banana'],\
['Alice','Bob','Carol','David'],\
['dogs','cats','moose','goose']]



colwidth = [0]*len(tabledata)
print(colwidth)


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
		print('colwidth',colwidth[i])
		i = i-1
		print(colwidth)

ptable(tabledata)
print(colwidth)
print(tabledata)

i = 3
while i > 0:
	print(tabledata[0][0].rjust(colwidth[0]) + ' ' + tabledata[1][0].ljust(colwidth[1]+1) + tabledata[2][0].ljust(colwidth[2]+1))
	

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

#printPicnic(picnicItems, 12, 5)
#printPicnic(picnicItems, 20, 6)

