import re
from bs4 import BeautifulSoup as bs
from requests import Session
f = open('post_datail.csv',mode='w',encoding='utf-8')
url = 'https://www.team-bhp.com/forum/official-new-car-reviews/126290-bmw-320d-328i-official-review-{}.html'
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
s = Session()
for j in range(1,140):
    try:
        m_url = url.format(j)
        r = s.get(m_url,headers=headers)
        soup = bs(r.content,'html.parser')
        tables = soup.find("div",attrs={"id":"posts"}).find_all("div",attrs={"style":"padding:0px 0px 6px 0px"})
        for i in tables:
            if(i.find('a','bigusername')):
                usn = i.find('a','bigusername').text.strip()
            else:
                usn = "Not given"
            pst = re.findall("Posts: (.*?)\s",str(i.find('td','alt2')))
            jn = re.findall("Join Date: (.*?)<",str(i.find('td','alt2')))
            thak = re.findall("Thanked: (.*?)\s",str(i.find('td','alt2')))
            loc = re.findall("Location: (.*?)<",str(i.find('td','alt2')))
            n = 'Username{}|Posts:{}|Join:{}|thanked:{}|locations:{}'.format(usn,pst,jn,thak,loc)
            f.write(n+'\n')
        print(m_url)
    except:
        pass
    
    # tb = soup.find_all('div',attrs={'style':'padding:0px 0px 6px 0px'})
    # for j in tb:        
    #         for k in j.find_all('div','smallfont'):
    #             # f.write(k.text.strip().replace('\r','').replace('\t','').replace('Team-BHP Support',''))



        # join = re.findall("Join Date: (.*?)<",i)
        # loc = re.findall("Location: (.*?)<",i)
        # post = re.findall("Posts: (.*?)<",i)
        # thak = re.findall("Thanked: (.*?)<",i)
        # n = 'Join data:{}|Location:{}|Post:{}|thanked:{}'.format(join,loc,post,thak)

        # if(j.find('a','bigusername')):
        #     usn = j.find('a','bigusername').text.strip()
        # else:
        #     usn = "Not given"

        # if(j.find('div','smallfont').next_sibling.next_sibling.next_sibling.next_sibling):
        #     join = j.find('div','smallfont').next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_element.next_element.next_element.next_element.next_element
        #     # .replace('\r','').replace('\t','').replace('\n','').replace('\xa0','').replace('  ','')
        # else:
        #     join = 'Not given'

        # if(j.find('div','smallfont').next_sibling.next_sibling.next_sibling.next_sibling):
        #     loc = j.find('div','smallfont').next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
        # else:
        #     loc = "Not given"
        
        # if(j.find('div','smallfont').next_sibling.next_sibling.next_sibling.next_sibling):
        #     posts = j.find('div','smallfont').next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
        # else:
        #     posts = 'Not given'
        
        # if(j.find('div','smallfont').next_sibling.next_sibling.next_sibling.next_sibling):
        #     thak = j.find('div','smallfont').next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.text.strip()
        # else:
        #     thak ='Not given'

        # np = 'username:{}|post details{}'.format(usn,)
        # f.write(np+'\n')
    # print(m_url)