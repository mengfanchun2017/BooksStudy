#7.18a-check-password.py

#later:
#and * when input
#ask twice for check

#input 放到 function外面的话是传递一个methord到function，len这样的不能使用
#放到里面赋值就ok了
import re

def checkps ():
    usrpass = input()
    if len(usrpass) < 8:
        print('you password lenth is:',len(usrpass))
        print('password lenth need more tnan 8, please input again:')
        checkps()
    re_match1 = re.compile(r'(\d+)')
    re_match2 = re.compile(r'([a-z]+)')
    re_match3 = re.compile(r'([A-Z]+)')
    find1 = re_match1.search(usrpass)
    find2 = re_match2.search(usrpass)
    find3 = re_match3.search(usrpass)
    #print(find1.group())
    #print(find2)
    #print(find3.group())
    #此处的print用于检查，当find为None时，group()会报错
    #若要使用的话，需要用try或者循环解决
    if not find1:
        print('no digital, input again:')
        checkps()
    if not find2:
        print('no a-z, input again:')
        checkps()
    if not find3:
        print('no A-Z, input again:')
        checkps()
    print('Password Accepted!')

print('\nPlease input your password:')
checkps()

#input()
#print(len(input()))

'''
raw_input = input()
print(raw_input)

print(type(raw_input))
print(len(raw_input))
'''
