#7.18b-strip-homemade.py
#re的源码
#https://stackoverflow.com/questions/452104/is-it-worth-using-pythons-re-compile/452142#452142
#正则和strip的结合使用
#google的python文档
#https://developers.google.com/edu/python/regular-expressions
#later:
#格式化字符串测试

import re

print('---testing strip---')
str1 = '   Got it! I said, I got it!   Do you hear me !!!   '
str2 = '!!!! I said, I got it!  !!!'
print(str1.strip())
print(str1.strip('!'))
print(str2.strip())
print(str2.strip('!'))

print('\n---使用连接符---')
#中间的|表示或者
def strip_new(text, chars=None):
    """去除首尾的字符

    :type text: string
    :type chars: string
    :rtype: string
    """
    if chars is None:
        reg = re.compile('^ *| *$')
    else:
        reg = re.compile('^[' + chars + ']*|[' + chars + ']*$')
    return reg.sub('', text)

print(strip_new('   123456   '))  # 123456
print(strip_new('   123456'))  # 123456
print(strip_new('   123456'))  # 123456
print(strip_new('123456   654321'))  # 123456   654321
print(strip_new('123456   654321', '1'))  # 23456   65432
print(strip_new('123456   654321', '1234'))  # 56   65
print(strip_new('123456   654321', '124'))  # 3456   6543

print('\n---strip manual---')
#如果使用r‘则会把里面的变量名当作字符看待，需要使用以下两种方式：
##使用连接符‘ + ’包围变量，并把变量放在[]中（自定义）
##使用格式化字符串"Hello %s !" % world完成
#使用group将find1找到的内容提取出来
#不加group的话就会得出match的输出
#compile不加（）分组的话，默认group（）== group（0）将显示所有匹配

def strip_man(string):
    re_match1 = re.compile(r'( )')
    find1 = re_match1.match(string)
    #print(matchkey)
    print(find1.group())
    print(type(str(find1)))
    print(len(find1.group()))

strip_man(str1)
