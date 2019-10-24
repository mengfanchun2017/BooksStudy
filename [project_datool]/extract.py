'''
function list:
1 /check df/
-1.1 checkdf(df) - 基准df信息输出
-1.2 checksample(df,random=42) - 对于列信息很多或者嵌套的,详细输出一个
2 /check column/
-2.1 checknest(df,colname) - 嵌套diclike信息输出
-2.2 checkvalue(df,list='all') - 检查指定列的value分布
3 /alter data/
-3.1 dorpcolumn(df,collist) - 删除列
'''

# prepare env
#需要使用 display 显示和 jupyter output 一样的样式
from IPython.display import display
import pprint as pp
#Pandas
import pandas as pd

def smaller_data(file,present=0.1,compress=NaN):
    if compress != NaN:
        
    if '.csv' in file:
        df = pd.read_csv(file)
        print(df.head())
    elseif '.json' in file:
        df = pd.read_json(file)
        print(df.head())
    elseif '.pickle' or '.pk' in file:
        df = pd.read_json(file)
        print(df.head())
