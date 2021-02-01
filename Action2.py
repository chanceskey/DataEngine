# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pandas import  DataFrame

data = {'Chinese': [68, 95, 98, 90,80], 'Math': [65, 76, 86, 88, 90], 'English': [30, 98, 88, 77, 90]}
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'LiuBei', 'DianWei', 'XuChu'], columns=['Chinese', 'Math', 'English'])

# 平均成绩
df = DataFrame(df2.mean(),columns=['mean'])
# 最小成绩
df["min"] = df2.min()
# 最大成绩
df["max"] = df2.max()
# 方差
df["var"] = df2.var()
# 标准差
df["std"] = df2.std()
print(df) # 输出成绩的均值，最小成绩，最大成绩，方差，标准差
# 总成绩排序
print("——————总成绩排序——————")
df3 = DataFrame(df2.sum(axis=1).sort_values(ascending=False),columns=['总成绩'])
df3["名次"] = range(1,6)

print(df3) # 输出成绩排名，名次

