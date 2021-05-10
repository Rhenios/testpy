import numpy
import matplotlib.pyplot as plt
import pandas as pd
import math
path = (来客数.csv)
df = pd.read_csv(path,index_col=0,encoding="shift-jis").VALUES
plt.hist(df)
plt.show()
