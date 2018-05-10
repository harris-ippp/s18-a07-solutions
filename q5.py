import pandas as pd

df = pd.read_csv('accidents2.csv')
operator_fatalities = df.groupby('Operator')['Fatalities count'].sum()

print(operator_fatalities.sort_values(ascending=False).head(1))
