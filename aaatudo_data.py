from bs4 import BeautifulSoup as bs
from requests import Session
import csv
s = Session()
f = open('aaauto_data123456.csv',mode='w',encoding='utf-8',newline="")
fr = open('aaa_links.txt',mode='r',encoding='utf-8')
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
row = csv.writer(f)
rd = fr.read().split()
for i in rd[4018:]:
    try:
        r = s.get(i,headers=headers)
        soup = bs(r.content,'html.parser')
        n1 = ''
        n2 = ''

        price = soup.find('strong','black notranslate')
        if(price):
            pr = soup.find('strong','black notranslate').text.strip()
        else:
            pr = 'Not given'

        name = soup.find('h1','h2 mb5')
        if(name):
            nm = soup.find('h1','h2 mb5').text.strip()
        else:
            nm = 'Not given'

        cname = soup.find('h1','h2 mb5')
        if(cname):
            cnam = soup.find('h1','h2 mb5').next_element.strip()
        else:
            cnam = 'Not given'
        
        tb = soup.find_all('table','transparentTable')
        if(len(tb) == 2):
            th1 = [a.text.strip() for a in tb[0].find_all('th')]
            td1 = [b.text.strip() for b in tb[0].find_all('td')]
            th2 = [c.text.strip() for c in tb[1].find_all('th')]
            td2 = [d.text.strip().replace('\t','').replace('\n','') for d in tb[1].find_all('td')]
            for x,y in zip(th1,td1):
                n1 += "{}:{}|".format(x,y)
            
            for j,k in zip(th2,td2):
                n2 += "{}:{}|".format(j,k)
        row.writerow([
            cnam,nm,pr,n1,n2,i
        ])
        print(i)
    # print(n1)
    # print(n2)
    except:
        pass