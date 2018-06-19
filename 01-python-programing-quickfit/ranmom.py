import random
word_list = ['tatoo', 'happy', 'apple', 'ios', 4]

def generate_password():
    return str(random.choice(word_list)) + str(random.choice(word_list)) + str(random.choice(word_list))
    #增加了str确保如果wordlist里面有4这样的数字可以转化为字符
print(generate_password())

def generate_password2():
    return ''.join(random.sample(word_list,5))
    #join方式就不能加str，要求wordlist都是字符，但是既然是wordlist就应该都保证是字符
    #而不是在写处理代码时候再额外处理不推进str的方式
print(generate_password2())
