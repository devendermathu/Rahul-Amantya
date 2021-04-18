from bs4 import BeautifulSoup as bs
from requests import Session
s = Session()
f = open('all_links2.txt',mode='w',encoding='utf-8')
url = 'https://www.cars.com/for-sale/searchresults.action/?page={}&perPage=50&rd=99999&searchSource=PAGINATION&sort=relevance&stkTypId=28880&zc=99501'
for i in range(1,51):
    m_url = url.format(i)
    r = s.get(m_url)
    soup = bs(r.content,'html.parser')
    ln = soup.find_all('div','shop-srp-listings__listing-container')
    for j in ln:
        l = j.find('a').get('href')
        f.write('https://www.cars.com'+l+'\n')
    print(m_url)