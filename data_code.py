from requests import Session
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import csv
fr = open('aaa.txt',mode='r',encoding='utf-8')
fd = open('all_data.csv',mode='w',encoding='utf-8',newline="")
rd = fr.read().split()
row = csv.writer(fd)
driver = webdriver.Firefox()
driver.get('https://www.auto1.com/en/')
for i in rd[:5]:
    driver.get(i)
    tbd = ''
    soup = bs(driver.page_source,'html.parser')
    tb = soup.find('div','car-data-table')
    if(tb):
        for j in tb.find_all('tr'):
            tbd += j.text.strip()+'|'
    else:
        tbd = "Not given"
    row.writerow([
        
    ])