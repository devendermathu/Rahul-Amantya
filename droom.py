from requests import Session
from bs4 import BeautifulSoup as bs
s = Session()
f = open('droomlink4.txt',mode='w',encoding='utf-8')
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
url = 'https://droom.in/cars/new?page={}&tab=grid&bucket=car&condition=new&display_category=All%20Cars&category=car'
for i in range(176,256):
    m_url = url.format(i)
    r = s.get(m_url,headers=headers)
    soup = bs(r.content,'html.parser')
    h = soup.find_all('h4','heading')
    for i in h:
        a = i.find('a')
        if(a == "None" or a =="none" or a == None):
            print('Noting')
        else:
            f.write(a.get('href')+'/features'+'\n')
    print(m_url)
