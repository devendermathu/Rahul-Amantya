from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import csv
import time
t = 5
f = open('12345.csv',mode='w',encoding='utf-8')
# enter_url = 'https://twitter.com/login'
# enter_url = 'https://twitter.com/search?q={}%20{}&src=typed_query'
driver = webdriver.Firefox()
driver.maximize_window()
# driver.get(enter_url.format('BMWMotorrad_IN',''))
driver.get('https://twitter.com/bmwmotorrad_in?lang=en')
time.sleep(5)
# search = driver.find_element_by_xpath('//a[@class="css-4rbku5 css-18t94o4 css-1dbjc4n r-sdzlij r-1loqt21 r-1adg3ll r-ahm1il r-1ny4l3l r-1udh08x r-o7ynqc r-6416eg r-13qz1uu"]')
# search.click()
# p = ''
for i in range(1,4):
    time.sleep(t)
    soup = bs(driver.page_source,'html.parser')
    art = soup.find_all('article','css-1dbjc4n r-1loqt21 r-18u37iz r-1ny4l3l r-o7ynqc r-6416eg')
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    for j in art:
        # if(j.text.endswith("h") == True):
            f.write(j.text.replace('\t','').replace('\r','').replace('\n','').replace(',','')+'\n')
            # p+=j.text.strip()

# print(p)

# last_height = driver.execute_script("return document.body.scrollHeight")
# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(10)
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#             break
# last_height = new_height


# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# action.move_to_element(search).perform()
# search = driver.find_element_by_xpath('//input[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-1sp51qo r-1swcuj1 r-1dz5y72 r-fdjqy7 r-13qz1uu"]')
# search.send_keys('audi india')
# search.send_keys(Keys.RETURN)
# driver.execute_script('arguments[0].scrollIntoView();',search)
# search.location_once_scrolled_into_view
# driver.execute_script("window.scrollto(0, document.body.scrollHeight);")