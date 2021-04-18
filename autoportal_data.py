from bs4 import BeautifulSoup as bs
from requests import Session
import csv
f = open('autop.csv',mode='w',encoding='utf-8',newline="")
s = Session()
row = csv.writer(f)
dt = ''
url = 'https://autoportal.com/newcars/toyota/etios/specifications/'
r = s.get(url)
soup = bs(r.content,'html.parser')
tb = soup.find_all('table','specifications-table')
if(tb):
    for i in tb:
        td = i.find_all('td')
        for j in td:
            dt+=j.text.strip()+'|'
            print(j.text.strip()+'|')
row.writerow([
    dt,url
])