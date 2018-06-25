##format methord
print('---test1:---')
print('I am lucky to eat {} {} {} {}!'.format(4,'eggs', 1, 'spam'))

print('---test2:---')
print('I am lucky to eat {2} {1} {3} {0}!'.format(4,'eggs', 1, 'spam'))

print('---test3:(option)---')
print('I am lucky to eat {2:.2f} {1} {3} {0}!'.format(4,'eggs', 1, 'spam'))

print('---test4:(option)---')
print('I am lucky to eat {2:.2f} {1:#^20} {3} {0}!'.format(
    4,'eggs', 1, 'spam'))

# variable methord compare
name = 'handsome'
print('hi {} !'.format(name))
#format后面可以跟列表和字典

print('hi ' + name + ' !')
print("hi " + name + " !")
print('hi', name, '!')
print("hi", name, "!")
