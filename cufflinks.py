import cufflinks as cf
import numpy as np
import pandas as pd
### 切换到本地画图
cf.go_offline()
###生成数据框并画图，kind指定画图类型，cf.help('kind')查看参数使用方法
cf.datagen.lines(4).iplot(kind='line', colors=['orange', 'teal', 'blue', 'red'])
###cf.datagen.box(4),默认生成100行数据，指定列数
df = pd.DataFrame(np.random.rand(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
df.iplot(kind='box', title='箱线图‘, legend=True, theme='solar', title='箱线图', xTitle='x', yTitle='y')
###cf.datagen.histogram(3),直方图
df.iplot(kind='histogram',theme='pearl',colors=['blue', 'yellow', 'cyan', 'green', 'purple'], legend='bottom')
###生成时间序列数据cf.datagen.lines(1, 500),3个不同周期时间序列曲线
cf.datagen.lines(1, 500).ta_plot(study='sma', periods=[13, 21, 55], mode='lines')
###散点图
df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
df.iplot(kind='scatter', mode='markers', colors=['orange', 'teal', 'blue', 'yellow'], size=10)
###气泡图
df.iplot('bubble', x='a', y='b', size='c')
###散点图矩阵
df.scatter_matrix(color='grey', size=5, theme=None)
###同时画多个图,产生子图
cf.datagen.lines(4).iplot(subplots=True, subplot_titles=True, legend=False, shared_xaxes=False, vertical_spacing=0.2, fill=True)

