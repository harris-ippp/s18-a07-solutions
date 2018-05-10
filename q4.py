import pandas as pd

df = pd.read_csv('accidents2.csv')
df_sorted = df.sort_values('Fatalities count', ascending=False)

print(df_sorted.head(1))
