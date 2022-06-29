import pandas as pd
import numpy as np

df = pd.read_excel('drug_order_detai_1.xlsx')
df['销售额'] = df['价格'] * df['销量']
result = df.groupby('分店')['销售额'].agg([np.min, np.max, np.mean])
print('所有分店总销售额是：', df['销量'].sum(), sep='')
print(result)
