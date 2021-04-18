from requests import Session
from bs4 import BeautifulSoup as bs
import csv
s = Session()
ul = []
more = []
param = []
f = open('get_links.txt',mode='r',encoding='utf-8')
fd = open('all_data.csv',mode='w',encoding='utf-8',newline="")
rd = f.read().split()
row = csv.writer(fd)

for i in rd[3300:]:
    try:
        r = s.get(i)
        ft = ''
        soup = bs(r.content,'html.parser')
        name = soup.find("h1","cui-heading-2--secondary vehicle-info__title")
        price = soup.find('span','vehicle-info__price-display vehicle-info__price-display--dealer cui-heading-2')
        ul = soup.find("ul","vdp-details-basics__list")
        table = soup.find("div","cpo-info__table")
        if(name):
            name = soup.find("h1","cui-heading-2--secondary vehicle-info__title").text
        else:
            name = "Not given"

        if(price):
            price = soup.find('span','vehicle-info__price-display vehicle-info__price-display--dealer cui-heading-2').text
        else:
            price = "Not given"

        features = ""
        p_detail = ''
        if(ul):
            for k in ul.find_all("li"):
                features += k.find("strong").text+" "+k.find("span").text+", "
        else:
            features = "Not given"
        if(table):
            for j in table.find_all('div'):
                p_detail += j.find('span','cpo-info__table-key').text +" "+j.find('span','cpo-info__table-value').text+","
        else:
            p_detail = "Not given"
        row.writerow([
            name,
            price,
            features,
            p_detail,
            i
        ])
        print(i)
    except:
        pass

    
            
    
    
    
    
    
    
    
    # # if(soup.find('ul','vdp-details-basics__list').find_all('span')[0]):
    # #     f1 = soup.find('ul','vdp-details-basics__list').find_all('span')[0].text
    # # else:
    # #     f1 = 'Not given'

    # # if(soup.find('ul','vdp-details-basics__list').find_all('span')[2]):
    # #     f2 = soup.find('ul','vdp-details-basics__list').find_all('span')[2].text
    # # else:
    # #     f2 = 'Not given'

    # # if(soup.find('ul','vdp-details-basics__list').find_all('span')[4]):
    # #     f3 = soup.find('ul','vdp-details-basics__list').find_all('span')[4].text
    # # else:
    # #     f3 = 'Not given'

    # # if(soup.find('ul','vdp-details-basics__list').find_all('span')[6]):
    # #     f4 = soup.find('ul','vdp-details-basics__list').find_all('span')[6].text
    # # else:
    # #     f4 = 'Not given'
    
    # # if(soup.find('ul','vdp-details-basics__list').find_all('span')[8]):
    # #     f5 = soup.find('ul','vdp-details-basics__list').find_all('span')[8].text
    # # else:
    # #     f5 = 'Not given'

    # # if(soup.find('ul','vdp-details-basics__list').find_all('span')[10]):
    # #     f6 = soup.find('ul','vdp-details-basics__list').find_all('span')[10].text
    # # else:
    # #     f6 = 'Not given'

    # # if(soup.find('ul','vdp-details-basics__list').find_all('span')[12]):
    # #     f7 = soup.find('ul','vdp-details-basics__list').find_all('span')[12].text
    # # else:
    # #     f7 = 'Not given'
    
    # # if(soup.find('ul','vdp-details-basics__list').find_all('span')[14]):
    # #     f8 = soup.find('ul','vdp-details-basics__list').find_all('span')[14].text
    # # else:
    # #     f8 = 'Not given'

    # # if(soup.find('ul','vdp-details-basics__list').find_all('span')[16]):
    # #     f9 = soup.find('ul','vdp-details-basics__list').find_all('span')[16].text
    # # else:
    # #     f9 = 'Not given'
    # nd = ''
    # ul  = soup.find_all('ul','details-feature-list__list')
    # for i in ul:
    #     li = i.find_all('li')
    #     for j in li:
    #         nd = nd+j.text
    
    # if(soup.find_all('span','cpo-info__table-value')[0]):
    #     mam = soup.find_all('span','cpo-info__table-value')[0].text
    # else:
    #     mam = 'Not given'
    
    # if(soup.find_all('span','cpo-info__table-value')[1]):
    #     bwt = soup.find_all('span','cpo-info__table-value')[1]
    # else:
    #     bwt = 'Not given'
    
    # if(soup.find_all('span','cpo-info__table-value')[2]):
    #     pwt = soup.find_all('span','cpo-info__table-value')[2]
    # else:
    #     pwt = 'Not given'
    
    # if(soup.find_all('span','cpo-info__table-value')[3]):
    #     dcr = soup.find_all('span','cpo-info__table-value')[3]
    # else:
    #     dcr = 'Not given'
    
    # if(soup.find_all('span','cpo-info__table-value')[4]):
    #     ra = soup.find_all('span','cpo-info__table-value')[4]
    # else:
    #     ra = 'Not given'
    # ntd = '{}|{}|{}|{}|{}|{}|{}|{}|{}'.format(name,price,nd,mam,bwt,pwt,dcr,ra,i)
    # fd.write(ntd+'\n')
    # print(i)
