from requests import Session
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
fn = open("noon.csv","r",encoding='utf-8')
fd = open('data5.csv',mode='w',encoding='utf-8')
# f_links=[]
# f_links1 =[]
# p = []
# p1 = []
f = 0
driver = webdriver.Firefox()
for p in fn:
    try:
        # f = f +1
        # if(f == 20):
        #     break
        driver.get(p)
        soup = bs(driver.page_source,'html.parser')
        something = [i.text for i in soup.find_all("strong","jsx-2119389001")]
        # price = [i.text for i in soup.find_all("span","value")]

        if(soup.find('span','jsx-4251264678 sellingPriceContainer').find('span','value')):
            p1 = soup.find('span','jsx-4251264678 sellingPriceContainer').find('span','value').text
        else:
            p1 = 'Not given'

        if(soup.find('div','jsx-2119389001 panelTrigger').find('span','value')):
            p2 = soup.find('div','jsx-2119389001 panelTrigger').find('span','value').text
        else:
            p2 = 'Not given'

        if(soup.find('h3','jsx-2803595502')):
            offer = soup.find('h3','jsx-2803595502').text.split()[0]
        else:
            offer = "Not given"

        image = []
        if(soup.find('img','jsx-193278340 fbn')):
            image = "Yes"
        elif(soup.find('div','jsx-193278340 container').find('img',attrs={'alt':'marketplace'})):
            image = "No"
        
        if(type(soup.find("strong","jsx-2119389001"))==None):
            ln = p
            f1 = p1
            offer1 = '1'
            im = image
            n = '{}|{}|{}|{}'.format(ln,f1,offer1,im)
            fd.write(n+'\n')
        else:
            for i in something:
                if(i=="Digital Upward"):
                    True
                else:
                    # f_links.append(p)
                    ln = p
                    im = image
                    if(p1>p2):
                        lw = p2
                        # f.write(p,p2)
                        n = '{}|{}|{}|{}'.format(ln,lw,offer,im)
                        fd.write(n+'\n')
                        # f_links1.append(p2)
                    elif(p2>p1):
                        lw = p1
                        n = '{}|{}|{}|{}'.format(ln,lw,offer,im)
                        fd.write(n+'\n')
    
    except:
        pass        # f_links1.append(p1)
                    # elif(p1 == p2):
                    #     lw = p1
                    #     n = '{}|{}|{}|{}'.format(ln,lw,offer,im)
                #     fd.write(n+'\n')


    print(p)
    print(p1)
    print(p2)
    # print(imae)

#print(f_links)
#print(len(f_links))
# df = pd.DataFrame({'Links':f_links1})
# print(list(set(f_links)))
# print(len(set(f_links)))

# print(len(f_links1))
# print(set(f_links1))
# print(price)