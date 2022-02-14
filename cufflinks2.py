import cufflinks as cf
import pandas as pd
import numpy as np
cf.go_offline()  ###cf.set_config_file(offline=True)
df = pd.DataFrame(np.random.randint(1, 10, (10, 3)), columns=['a', 'b', 'c'])
###条形图，barmode可选stack,overlay,group
df.iplot(kind='bar', barmode='group')
###
data = cf.datagen.bubble(10, 50, mode='stock')
figs = cf.figures(data, [dict(kind='histogram', keys='x', color='blue'),
                dict(kind='scatter', mode='markers', x='x', y='y', size=5),
                dict(kind='bar', barmode='group', color='teal')], asList=True)
figs.append(cf.datagen.lines(3).figure(legend=True))
pic = cf.subplots(figs)
cf.iplot(pic)

