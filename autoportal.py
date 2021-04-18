from requests import Session
from bs4 import BeautifulSoup as bs
s = Session()
f = open('link1.txt',mode='w',encoding='utf-8')
url = 'https://autoportal.com/newcars/cars-between-5-lakh-to-10-lakh+sedan-cars-in-india-cf/page/{}/'
for j in range(1,17):
    m_url = url.format(j)
    r = s.get(m_url)
    soup = bs(r.content,'html.parser')
    p = soup.find_all('p','h1 model-title')
    for i in p:
        a = i.find('a').get('href')
        f.write('https://autoportal.com'+a+'specifications/'+'\n')
    print(m_url)