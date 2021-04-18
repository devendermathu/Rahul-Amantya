from bs4 import BeautifulSoup as bs
from requests import Session
s = Session()
ff = open('all_links.txt',mode='r',encoding='utf-8')
fd = open('dta.txt',mode='w',encoding='utf-8')
rd = ff.read().split()
for i in rd[:10]:
    r = s.get(i)
    soup = bs(r.content,'html.parser')
    tit = soup.find('h1','cui-page-section__title').text
    price = soup.find('div','mmy-header__msrp mmy-header__info-border').text.replace('\n','').replace('MSRP','').split()
    # pteg = soup.find('div','warranty-section new-warranty').find_all('p')
    if(soup.find('div','warranty-section new-warranty').find_all('p')[0]):
        btb = soup.find('div','warranty-section new-warranty').find_all('p')[0].text
    else:
        btb = 'Not given'

    if(soup.find('div','warranty-section new-warranty').find_all('p')[1]):
        btbd = soup.find('div','warranty-section new-warranty').find_all('p')[1].text
    else:
        btbd = 'Not given'

    if(soup.find('div','warranty-section new-warranty').find_all('p')[2]):
        ptrain = soup.find('div','warranty-section new-warranty').find_all('p')[2].text
    else:
        ptrain = 'Not given'

    if(soup.find('div','warranty-section new-warranty').find_all('p')[3]):
        ptraind = soup.find('div','warranty-section new-warranty').find_all('p')[3].text
    else:
        ptraind = 'Not given'

    if(soup.find('div','warranty-section new-warranty').find_all('p')[4]):
        raistan = soup.find('div','warranty-section new-warranty').find_all('p')[4].text
    else:
        raistan = 'Not given'

    if(soup.find('div','warranty-section new-warranty').find_all('p')[5]):
        raistand = soup.find('div','warranty-section new-warranty').find_all('p')[5].text
    else:
        raistand = 'Not given'
    

    if(soup.find('div','warranty-section cpo-warranty').find_all('p')[0]):
        mam = soup.find('div','warranty-section cpo-warranty').find_all('p')[0].text
    else:
        mam = 'Not given'
    
    if(soup.find('div','warranty-section cpo-warranty').find_all('p')[1]):
        mamd = soup.find('div','warranty-section cpo-warranty').find_all('p')[1].text
    else:
        mamd = "Not given"
    
    if(soup.find('div','warranty-section cpo-warranty').find_all('p')[2]):
        bwt = soup.find('div','warranty-section cpo-warranty').find_all('p')[2].text
    else:
        bwt = "Not given"
    
    if(soup.find('div','warranty-section cpo-warranty').find_all('p')[3]):
        bwtd = soup.find('div','warranty-section cpo-warranty').find_all('p')[3].text
    else:
        bwtd = "Not given"
    
    if(soup.find('div','warranty-section cpo-warranty').find_all('p')[4]):
        pwt = soup.find('div','warranty-section cpo-warranty').find_all('p')[4].text
    else:
        pwt = "Not given"

    if(soup.find('div','warranty-section cpo-warranty').find_all('p')[5]):
        pwtd = soup.find('div','warranty-section cpo-warranty').find_all('p')[5].text
    else:
        pwtd = "Not given"

    if(soup.find('div','warranty-section cpo-warranty').find_all('p')[6]):
        dcr = soup.find('div','warranty-section cpo-warranty').find_all('p')[6].text
    else:
        dcr = "Not given"

    if(soup.find('div','warranty-section cpo-warranty').find_all('p')[7]):
        dcrd = soup.find('div','warranty-section cpo-warranty').find_all('p')[7].text
    else:
        dcrd = "Not given"

    if(soup.find('div','warranty-section cpo-warranty').find_all('p')[8]):
        ra = soup.find('div','warranty-section cpo-warranty').find_all('p')[8].text
    else:
        ra = "Not given"
    
    if(soup.find('div','warranty-section cpo-warranty').find_all('p')[9]):
        rad = soup.find('div','warranty-section cpo-warranty').find_all('p')[9].text
    else:
        rad = "Not given"
    

    
    dt = '{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}'.format(tit,price,btb,btbd,ptrain,ptraind,raistan,raistand,mam,mamd,bwt,bwtd,dcr,dcrd,ra,rad,i)
    fd.write(dt+'\n')
    print(i)