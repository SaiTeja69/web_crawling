import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import pandas as pd
import csv

url_main='https://oriparts.com/42/344/2746/753011'
response = requests.get(url_main)
screp = BeautifulSoup(response.text, 'html.parser')
screp.findAll('a')
websites=[]
for i in range(4,len(screp.findAll('a'))):
    tag = screp.findAll('a')[i]
    websites.append(tag['href'])
import pandas as pd
df = pd.DataFrame(websites, columns=["colummn"])
df.to_csv('websites.csv', index=False)