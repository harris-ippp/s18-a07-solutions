import pandas as pd
import re

number = re.compile('\d+')

def get_first_number(text):
    if pd.isnull(text):
        return None
    
    matches = number.findall(text)
    if len(matches) == 0:
        return None
    else:
        return matches[0]

df = pd.read_csv('accidents.csv')
df['Fatalities count'] = df['Fatalities'].apply(get_first_number)

df.to_csv('accidents2.csv', index=False)
