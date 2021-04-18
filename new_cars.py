from bs4 import BeautifulSoup as bs
from requests import Session
s = Session()
s.headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'
f = open('new_cars_zhidou.txt',mode='w',encoding='utf-8')
url = 'https://www.autoscout24.com/lst/others?sort=standard&desc=0&offer=N&ustate=N%2CU&size=20&page={}&atype=C&'
for i in range(1,14):
    m_url = url.format(i)
    r = s.get(m_url)
    soup = bs(r.content,'html.parser')
    div = soup.findAll('div','cldt-summary-titles')
    for j in div:
        a = j.find('a')
        f.write('https://www.autoscout24.com'+a.get('href')+'?cldtidx=1&cldtsrc=listPage'+'\n')
    print(m_url)