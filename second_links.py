from requests import Session
from bs4 import BeautifulSoup as bs
s = Session()
fd = open('second_all_data.txt',mode='w',encoding='utf-8',newline="")
url = 'https://driverbase.com/inventory?search.SortTypeId=3&search.DealershipId=0&search.Zip=10010&search.DistanceFromZip=100&search.InventoryType=all&search.MakeId=0&search.ModelId=-1&search.VehicleBodyTypeId=0&search.YearMin=1980&search.YearMax=2020&search.PriceMinString=%241%2C000&search.PriceMaxString=%24100%2C000%2B&search.MpgMinString=0&search.MpgMaxString=100%2B&search.MileageMinString=0&search.MileageMaxString=200%2C000%2B&search.RequireImages=true&search.PropulsionTypeId=0&search.CabTypeId=0&search.SIdx={}&search.EIdx={}&search.Prev=true'
st = 3061
en = 3075
for j in range(1,400):
    m_url = url.format(st,en)
    r = s.get(m_url)
    soup = bs(r.content,'html.parser')
    td = soup.find_all('td','valign-middle col-sm-4')
    for i in td:
        a = i.find('a')
        fd.write('https://driverbase.com'+a.get('href')+'\n')
    st +=15
    en +=15
    print(st)
    print(en)
    # print(j)
    print(m_url)
    # print(j)
