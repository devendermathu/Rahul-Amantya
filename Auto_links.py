from requests import Session
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
ur1 = 'https://www.auto1.com/en/'
ur2 = 'https://www.auto1.com/en/app/merchant/cars?channel=24h&dir=desc&page={}&sort=popularity'
f = open('A_links.txt',mode='w',encoding='utf-8')
driver = webdriver.Firefox()
driver.get(ur1)
for i in range(17,101):
    try:
        m_url = ur2.format(i)
        driver.get(m_url)
        time.sleep(10)
        soup = bs(driver.page_source,'html.parser')
        div = soup.find_all('div','big-car-card__title big-car-card__title--bottom')
        for j in div:
            a = j.find('a')
            f.write('https://www.auto1.com'+a.get('href')+'\n')
        print(m_url)
    except:
        pass
