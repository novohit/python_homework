import numpy as np
import pandas as pd

np.random.seed(int(input(), 16))
data = np.random.normal(loc=75, scale=8, size=(40, 4))
df = pd.DataFrame(data.astype(np.intc), index=[i + 1001 for i in range(40)],
                  columns=[chr(i) for i in range(ord('A'), ord('D') + 1)])
print(df.head(5))
