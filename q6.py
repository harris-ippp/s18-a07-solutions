import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('accidents.csv')
dates = pd.to_datetime(df['Date'], errors='coerce')

dates.dt.year.value_counts().sort_index().plot()
plt.savefig('years.png')
