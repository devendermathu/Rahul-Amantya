from bs4 import BeautifulSoup as bs
from requests import Session
import csv
s = Session()
f = open('carstrade_data3.csv',mode='w',encoding='utf-8',newline="")
fd = open('cartrade_links.txt',mode='r',encoding='utf-8')
rd = fd.read().split()
row = csv.writer(f)
for i in rd[5568:]:
    try:
        r = s.get(i)
        soup = bs(r.content,'html.parser')
        nm = ''
        pr = ''
        tbl = ''
        name = soup.find('h1','h_2')
        price = soup.find('span','rupee_font font_20').next_element.next_element.next_element
        tb = soup.find_all('table','v_table')
        if(name):
            nm = soup.find('h1','h_2').text
        else:
            nm = 'Not given'
        if(price):
            pr = price = soup.find('span','rupee_font font_20').next_element.next_element.next_element.text
        else:
            pr = "Not given"
        for j in tb:
            tr = j.find_all('tr')
            for k in tr:
                tbl +=k.text+'|'

        row.writerow([
            nm,
            pr,
            tbl,
            i
        ])
        print(i)
    except:
        pass

