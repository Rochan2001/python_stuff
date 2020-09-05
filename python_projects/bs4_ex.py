import requests
from bs4 import BeautifulSoup

source = requests.get(
    'https://pythonprogramming.net/parsememcparseface/')
soup = BeautifulSoup(source.content,"html.parser")
table = soup.table
table_rows = soup.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)
dfs = pd.read_html("https://pythonprogramming.net/parsememcparseface/",header=1)
for df in dfs:
    print(df)
    
