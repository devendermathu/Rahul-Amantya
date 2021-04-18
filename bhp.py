from bs4 import BeautifulSoup as bs
from requests import Session
import re
import csv
s = Session()
f = open('chevrolet_sheet6.csv',mode='w',encoding='utf-8')
url = 'https://www.team-bhp.com/forum/test-drives-initial-ownership-reports/224958-driven-audi-a8l-review-3-0-v6-turbo-petrol-{}.html'
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
for k in range(1,3):
    try:
        m_url = url.format(k)
        r = s.get(m_url,headers=headers)
        soup = bs(r.content,'html.parser')
        tb = soup.find_all('div',attrs={'style':'padding:0px 0px 6px 0px'})
        for i in tb:
            if(i.find('div','smallfont')):
                teams = i.find('div','smallfont').text
            else:
                teams = "Not given"
            if(i.find('hr').previous_element.previous_element.previous_element.previous_element):
                off = i.find('hr').previous_element.previous_element.previous_element.previous_element
            else:
                off = "Not given"
            if(i.find('a','bigusername')):
                usn = i.find('a','bigusername').text.strip()
            else:
                usn = "Not given"
            if(i.find('td','thead')):
                post_date = i.find('td','thead').text.strip()
            else:
                post_date = "Not given"
            if(i.find('hr').next_element.next_element.text.strip()):
                twit = i.find('hr').next_element.next_element.text.strip().replace('\t','').replace('\r','').replace('\n','').replace(', ','').replace(';','').replace('  ','').replace('; ','')
            else:
                twit = "not given"

            if(re.findall("Posts: (.*?)\s",str(i.find('td','alt2')))):
                pst = re.findall("Posts: (.*?)\s",str(i.find('td','alt2')))
            else:
                pst = 'Not given'

            if(re.findall("Join Date: (.*?)<",str(i.find('td','alt2')))):
                jn = re.findall("Join Date: (.*?)<",str(i.find('td','alt2')))
            else:
                jn = 'Not given'
            if(re.findall("Thanked: (.*?)\s",str(i.find('td','alt2')))):
                thak = re.findall("Thanked: (.*?)\s",str(i.find('td','alt2')))
            else:
                thak = 'Not given'
            if(re.findall("Location: (.*?)<",str(i.find('td','alt2')))):
                loc = re.findall("Location: (.*?)<",str(i.find('td','alt2')))
            else:
                loc = "Not given"
            dt = '{}|Posts:{}|Join{}|Thanked:{}|Loction:{}|{}|{}|{}|{}'.format(post_date,pst,jn,thak,loc,usn,teams,off,twit)
            f.write(dt+'\n')
            # dt = '{}|{}|{}|{}'.format(pst,jn,thak,loc)
            # print(dt)
            # print(post_datail)
        print(m_url)
    except:
        pass

