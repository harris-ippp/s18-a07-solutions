import pandas as pd

df = pd.read_csv('accidents.csv')
print(df['Flight origin'].value_counts().head(1))
