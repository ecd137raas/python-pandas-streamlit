import pandas as pd
import numpy as np

df = pd.read_excel('sales-funnel.xlsx')
print(df.head())

pd.pivot_table(df,index=["Name","Rep","Manager"])

print(df.head())
