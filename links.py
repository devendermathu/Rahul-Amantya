from bs4 import BeautifulSoup as bs
from requests import Session
f = open('link_A_only.txt',mode='w',encoding='utf-8')

s = Session()
# url = 'https://www.cars.com/research/coupe/?pageNum=0&rpp={}'
url = 'https://www.cars.com/research/truck/?pageNum=0&rpp=59'
# for j in range(1,101):
#     m_url = url.format(j)
r = s.get(url)
soup = bs(r.content,'html.parser')
ln = soup.find_all('div','card-link-section')
for i in ln:
    n = i.find('a').get('href')
    d = 'https://www.cars.com/{}'.format(n)
    f.write(d+'\n')
print(url)