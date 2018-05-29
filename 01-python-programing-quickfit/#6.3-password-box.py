#! python3
# pw.py - An insecure password locker program.
## first line is used to work with sys.argv
## sys.argv brief
## http://www.cnblogs.com/cython/articles/2196715.html
## example in books show a wrong pic, code is ok. Beautiful output!
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)



## problems: sys not recg #! python3, later
