import pandas as pd

df = pd.read_csv('accidents.csv')
print(df['Operator'].value_counts().head(1))
