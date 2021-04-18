from bs4 import BeautifulSoup as bs
from requests import Session
# import csv
s = Session()
f = open('cartrade_links_ghaziabad.txt',mode='w',encoding='utf-8')
url = 'https://www.cartrade.com/buy-used-cars/ghaziabad/c/p-{}'
for i in range(1,23):
    m_url = url.format(i)
    r = s.get(m_url)
    lnk = ''
    soup = bs(r.content,'html.parser')
    ln = soup.find_all('h2','h2heading')
    if(ln):
        for j in ln:
            a = j.find('a').get('href')
            f.write('https://www.cartrade.com'+a+'\n')
    else:
        lnk = "Not given"
    print(m_url)


