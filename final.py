import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import pandas as pd
header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}


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
k=1
for i in websites:
    r = requests.get(str(i), headers=header)
    dfs = pd.read_html(r.text)
    a = dfs[0]
    a.to_csv(r"oriparts{}.csv".format(k))
    k+=1
