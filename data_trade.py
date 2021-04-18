from bs4 import BeautifulSoup as bs
from requests import Session
import csv
f = open('tradeindia.csv',mode='w',newline="")
row = csv.writer(f)
s = Session()
url = 'https://www.tradeindia.com/products/plastic-grip-tongue-cleaner-c3684036.html'
r = s.get(url)
soup = bs(r.content,'html.parser')
d1 = ''
d2 = ''
allD = ''
ul = soup.find_all('ul','list flex flex-wrap mb30 fs17')
if(len(ul) == 2):
    ul1 = ul[0].find_all('span')
    ul2 = ul[1].find_all('span')
    for i in ul1:
        d1 += i.text+','

    for i in ul2:
        d2 += i.text+','
elif(ul):
    if(ul):
        for i in ul:
            li = i.find_all('li')
            for j in li:
                allD += j.text
                allD.split()
    else:
        d1 = 'Not given'
        d2 = "Not given"
else:
    d1 = 'Not given'
    d2 = 'Not given'
    allD = 'Not given'
d2.split()
d1.split()
row.writerow([
    d1,
    d2,
    allD,
    i
])
print(url)