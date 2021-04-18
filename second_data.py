from requests import Session
from bs4 import BeautifulSoup as bs
import csv
s = Session()
fd = open('all_data123.csv',mode='w',encoding='utf-8',newline="")
f = open('second_all_data222.txt',mode='r',encoding='utf-8',newline="")
rd = f.read().split()
row = csv.writer(fd)
for i in rd[3056:]:
    try:   
        # r = s.get('https://driverbase.com/vehicle/2534402/2017-audi-a4-in-long-island-city-ny/WAUENAF4XHN006827')
        r = s.get(i)
        soup = bs(r.content,'html.parser')
        name = soup.find('h2','col-xs-8').text
        price = soup.find('h2','col-xs-4 green')
        if(price):
            price = soup.find('h2','col-xs-4 green').text
        else:
            price = "Not given"
        
        if(name):
            name = soup.find('h2','col-xs-8').text
        else:
            name = "Not given"
        table = soup.find('table','table table-striped table-hover')
        tb = ''
        if(table):
            for k in table.find_all('tr'):
                for j in k.find_all('td'):
                    tb+=j.text
        else:
            tb ='Not given'
        row.writerow([
        name,
        price,
        tb,
        i
        ])
        print(i)
    except:
        pass