import pandas as pd

# Change False to True for this block of code to see what it does

# DataFrame applymap()
if 0:
    df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [10, 20, 30],
        'c': [5, 10, 15]
    })

    def add_one(x):
        return x + 1

    print (df.applymap(add_one))
    # 就是把df的每个元素都运行一遍add_one函数

grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio',
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)

def convert_grades(grades):
    '''
    Fill in this function to convert the given DataFrame of numerical
    grades to letter grades. Return a new DataFrame with the converted
    grade.

    The conversion rule is:
        90-100 -> A
        80-89  -> B
        70-79  -> C
        60-69  -> D
        0-59   -> F
    '''
    if grades >= 90:
        grades = 'A'
        return 'A'
         # 注意这里F是字符，如果不加引号，python会报错找不到F这个变量
    elif 60 <= grades <= 69:
        grades = 'D'
    elif 70 <= grades <= 79:
        grades = 'C'
    elif 80 <= grades <= 89:
        grades = 'B'
    elif 90 <= grades <= 100:
        grades = 'A'
    else:
         pass
    return grades

print(grades_df)
grades_df.applymap(convert_grades)
# 如果不使用.apply,而直接把df作为输入，就会报错：
# ValueError: The truth value of a DataFrame is ambiguous.
# 因为不知道要怎么处理df中的那么多数据，apply就明确的说每个都要处理
print(grades_df)
