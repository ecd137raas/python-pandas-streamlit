import pandas as pd

df=pd.read_csv("cars.csv", sep=",")

print(df.head())
print(df.info())
