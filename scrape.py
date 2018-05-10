import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_table_data(a_page, header):
    """
    Given an accident page and a table header, get the corresponding data
    """
    try:
        th = a_page.find('th', text=header)
        return th.find_next('td').text
    except:
        print(header)
        return None
    
def get_data(a):
    """
    Given an accident link, return a dictionary of data from the infobox
    """
    a_path = a.attrs['href']
    a_response = requests.get(base + a_path)
    a_page = BeautifulSoup(a_response.text, 'html.parser')

    headers = ['Date', 'Operator', 'Flight origin', 'Destination', 'Fatalities']
    data = {'Name': a.text}
    for header in headers:
        data[header] = get_table_data(a_page, header)
    
    return data

base = 'https://en.wikipedia.org'
path = '/wiki/List_of_accidents_and_incidents_involving_commercial_aircraft'

response = requests.get(base + path)
page = BeautifulSoup(response.text, 'html.parser')

# get all of the bold tags
# ignore the last one because its an internal link
bolds = page.find_all('b')[-1]

data = []
for b in bolds:
    print(b.text) # print the current tag's text to display progress
    a = b.find('a') # find the link
    if a is None: # if the link is None, skip
        print('No link')
    else:
        data.append(get_data(a))
        time.sleep(1) # sleep between requests

df = pd.DataFrame(data)
df.drop_duplicates(inplace=True) # some accidents are linked more than once
df.to_csv('accidents.csv', index=False)
