#7.15-cell-email-regex


#贪心模式是在范围匹配后面加一个？
#除了search还有findall（后者是匹配全部）
#可以建立自己的字符分类
#.代表一个除换行之外的所有字符（如果要匹配换行，可以传入re.I）
#*代表重复前面0次任意次（属于贪心模式），所以.*就是代表所有字符的通配符
#复杂的正则可以使用re.VERBOSE调用方式
#r‘’‘（ ）‘’’，内容可以每个内容断行一次，注意前面是‘’‘
#调用时候要后面带re.VERBOSE说明
#http://www.diveintopython.net/regular_expressions/verbose.html
#regex中文文档摘译
#http://www.cnblogs.com/jcli/archive/2013/06/16/3137798.html
#regex先compile后match的好处：分离rex和使用，可充用变量，节省时间，参考链接：
#https://stackoverflow.com/questions/452104/is-it-worth-using-pythons-re-compile/452142#452142
#推荐！在线regex练习：https://regexr.com

'''
?匹配零次或一次前面的分组
*匹配零次或多次前面的分组
+匹配一次或多次前面的分组
{n}匹配n次前面的分组
{n,}匹配n次或更多前面的分组
{,m}匹配零次到m次前面的分组
{n,m}匹配至少n次、至多m次前面的分组
{n,m}?或*?或+?对前面的分组进行非贪心匹配
^spam意味着字符串必须以spam开始
spam$意味着字符串必须以spam结束
.匹配所有字符，换行符除外
\d、\w和\s分别匹配数字、单词和空格
\D、\W和\S分别匹配出数字、单词和空格外的所有字符
[abc]匹配方括号内的任意字符（诸如a、b或c)
[^abc]匹配不在方括号内的任意字符
'''

import pyperclip, re

print('---test1---')
#group() 默认为（0）即是所有的group。如果要以元祖方式显示，可以用groups
phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo = phoneNumRegex.search('My number is 415-555-4222.')
print('Phone number found: ' + mo.group())
print(mo.group())
print(mo.groups())
print(type(mo.groups()))

print('\n---test2-sub---')
agentNamesRegex = re.compile(r'Agent (\w)\w*')
printtemp = agentNamesRegex.sub(r'\1****', \
'Agent Alice told Agent Carol that AgentEve knew Agent Bob was a double agent.')
print(printtemp)

print('\n---function1---')
def name_of_email(addr):
    re_match = re.compile(r'(\w)*@(\w)*.(\w)*')
    find = re_match.search(addr)
    print(find.group())
name_of_email('<Tom Paris> tom@voyager.org')

print('\n---solution1(latin)---')
# copy到汉字回报decoding错误，后续研究pyperclber
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)?         # separator
    (\d{3})              # first 3 digits
    (\s|-|\.)          # separator
    (\d{4})              # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

# Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4}){1,2} # dot-something
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

# 使用re.UNICODE还是报错，再研究吧（用了UNI就不能用VERBOSE）
'''
print('\n---solution2(Unicode)---')
# copy到汉字回报decoding错误，后续研究pyperclber
# Create phone regex.
phoneRegex = re.compile(r'(\d{3}|\(\d{3}\))?(\s|-|\.)?(\d{3})(\s|-|\.)(\d{4})(\s*(ext|x|ext.)\s*(\d{2,5}))?', re.UNICODE)

# Create email regex.
emailRegex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}){1,2}', re.UNICODE)

# Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
'''
