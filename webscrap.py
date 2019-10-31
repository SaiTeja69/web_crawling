import requests
import pandas as pd
header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}
a = """https://oriparts.com/42/344/2746/753284
https://oriparts.com/42/344/2746/753281
https://oriparts.com/42/344/2746/753278
https://oriparts.com/42/344/2746/753285
https://oriparts.com/42/344/2746/753287
https://oriparts.com/42/344/2746/753283
https://oriparts.com/42/344/2746/753280
https://oriparts.com/42/344/2746/753277
https://oriparts.com/42/344/2746/753286
https://oriparts.com/42/344/2746/753279
https://oriparts.com/42/344/2746/753282"""
a = a.split("\n")

k=10
for i in a:
    r = requests.get(i, headers=header)
    dfs = pd.read_html(r.text)
    a = dfs[0]
    a.to_csv(r"oriparts{}.csv".format(k))
    k+=1