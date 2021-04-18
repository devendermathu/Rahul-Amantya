from requests import Session
from bs4 import BeautifulSoup as bs
from lxml import html
import csv
import re
import time
l = []
s = Session()
s.headers['User-Agent']="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"
fw = open('outputfile.csv','w',encoding='utf-8',newline="")
row = csv.writer(fw)
row.writerow(['Available','Brand','Category','Country','Display','Extrat_Date','Graphics','Hard_Drive','Momery_card','Model_name','Operating_System','Processor','Description','Regular_price','Retailer','SKU','Sales_price','Battery','Bluethooth','Product_url','warranty'])
# last= 'https://www.dell.com/en-au/shop/2-in-1-laptops/sr/dell-tablets/xps-2-in-1?page={}'
url = ['https://www.dell.com/en-au/shop/dell-laptops/sr/laptops/inspiron-laptops?page={}','https://www.dell.com/en-au/shop/dell-laptops/sr/laptops/xps-laptops?page={}','https://www.dell.com/en-au/shop/dell-laptops/sr/laptops/g-series?page={}','https://www.dell.com/en-au/shop/dell-laptops/sr/laptops/alienware-laptops?page={}','https://www.dell.com/en-au/shop/gaming-and-games/sr/game-laptops/g-series?page={}','https://www.dell.com/en-au/shop/gaming-and-games/sr/game-laptops/alienware-laptops?page={}','https://www.dell.com/en-au/shop/2-in-1-laptops/sr/dell-tablets/inspiron-2-in-1?page={}']
# ,'https://www.dell.com/en-au/shop/dell-laptops/sr/laptops/xps-laptops?page={}']
# n_url = ['https://www.dell.com/en-au/shop/dell-laptops/sr/laptops/xps-laptops']
# ,'https://www.dell.com/en-au/shop/dell-laptops/sr/laptops/xps-laptops']
al_tf=True
main_lnk=[]
cat_lnk=[]


def last_link(r):
	lnk = tree.xpath('//h3[@class="ps-title"]//a//@href')
	for j in lnk:
		l.append(j)
	return l


def To_data(response):
	r = s.get(response)
	tree = html.fromstring(r.text)
	soup = bs(r.content,'html.parser')
	Avail = 'Available'
	brand = 'Dell'
	category="Laptops"
	country="AU"
	mrp_price = ''.join(tree.xpath('//span[@class="cf-price strikethrough"]//text()')).strip()
	sales_price = ''.join(tree.xpath('//div[@class="cf-price js-tooltip-trigger"]//text()')).strip()
	# discount = float(mrp_price.replace('$','').replace('.','').replace(',','')) - float(sales_price.replace('$','').replace('.','').replace(',',''))
	display = ''.join(tree.xpath('//div[@class="row cf-module-wrap"]//h4[contains(string(),"Display")]//ancestor::div[@class="col col-md-4 cf-module-left-col"]//following-sibling::div//div[@class="cf-options-wrap  "]//div[@class="cf-read-only-wrap"]//following-sibling::div[not(@class)]//text()')).strip()
	ex_date = time.strftime("%Y-%m-%d")
	graphics = ''.join(tree.xpath('//div[@class="row cf-module-wrap"]//h4[contains(string(),"Video Card")]//ancestor::div[@class="col col-md-4 cf-module-left-col"]//following-sibling::div//div[@class="cf-options-wrap  "]//div[@class="cf-read-only-wrap"]//following-sibling::div[not(@class)]//text()')).strip()
	hard_driver = ''.join(tree.xpath('//div[@class="row cf-module-wrap"]//h4[contains(string(),"Hard Drive")]//ancestor::div[@class="col col-md-4 cf-module-left-col"]//following-sibling::div//div[@class="cf-options-wrap  "]//div[@class="cf-read-only-wrap"]//following-sibling::div[not(@class)]//text()')).strip()
	momery_card = ''.join(tree.xpath('//div[@class="row cf-module-wrap"]//h4[contains(string(),"Memoryi")]//ancestor::div[@class="col col-md-4 cf-module-left-col"]//following-sibling::div//div[@class="cf-options-wrap  "]//div[@class="cf-read-only-wrap"]//following-sibling::div[not(@class)]//text()')).strip()
	model_name = ''.join(tree.xpath('//h1[@class="cf-pg-title"]//span//text()')).strip()
	operating_system = ''.join(tree.xpath('//div[@class="row cf-module-wrap"]//h4[contains(string(),"Operating System")]//ancestor::div[@class="col col-md-4 cf-module-left-col"]//following-sibling::div//div[@class="cf-options-wrap  "]//span[@class="block cf-opt-body"]//label//text()')).strip()
	processer= ''.join(tree.xpath('//div[@class="row cf-module-wrap"]//h4[contains(string(),"Processor")]//ancestor::div[@class="col col-md-4 cf-module-left-col"]//following-sibling::div//div[@class="cf-options-wrap  "]//div[@class="cf-read-only-wrap"]//following-sibling::div[not(@class)]//text()')).strip()
	project = 'will get'
	retailer = 'Dell'
	description = ''.join(tree.xpath('//div[@class="col cf-feature-wrap ImageTop   "]//div//div[@class="cf-f-item-desc"]//text()')).strip() +" "+''.join(tree.xpath('//div[@class="col cf-feature-wrap TextRightImageLeft   "]//div[@class="cf-f-item-desc"]//text()'))+" "+''.join(tree.xpath('//div[@class="col cf-feature-wrap TextLeftImageRight   "]//div[@class="cf-f-item-desc"]//text()')).strip()
	project = "wil get"
	sku_id = ''.join(re.findall(',"sku":"(.*?)","brand":',r.text)).strip()
	battery = ''.join(tree.xpath('//div[@class="row cf-module-wrap"]//h4[contains(string(),"Primary Battery")]//ancestor::div[@class="col col-md-4 cf-module-left-col"]//following-sibling::div//div[@class="cf-options-wrap  "]//div[@class="cf-read-only-wrap"]//following-sibling::div[not(@class)]//text()')).strip()
	bluethooth = ''.join(tree.xpath('//div[@class="row cf-module-wrap"]//h4[contains(string(),"Primary Wireless")]//ancestor::div[@class="col col-md-4 cf-module-left-col"]//following-sibling::div//div[@class="cf-options-wrap  "]//div[@class="cf-read-only-wrap"]//following-sibling::div[not(@class)]//text()')).strip()
	# ctg_links = cat_links
	warranty = tree.xpath('//div[@class="row cf-module-wrap"]//h4[contains(string(),"Warranty")]//ancestor::div[@class="col col-md-4 cf-module-left-col"]//following-sibling::div//div[@class="cf-options-wrap  "]//following-sibling::div[@class="cf-options-group-wrap"]//h5[@class="cf-option-group-title"][1]//ancestor::div[@class="cf-options-group-wrap"]//label//text()')
	if(warranty):
		wnty = tree.xpath('//div[@class="row cf-module-wrap"]//h4[contains(string(),"Warranty")]//ancestor::div[@class="col col-md-4 cf-module-left-col"]//following-sibling::div//div[@class="cf-options-wrap  "]//following-sibling::div[@class="cf-options-group-wrap"]//h5[@class="cf-option-group-title"][1]//ancestor::div[@class="cf-options-group-wrap"]//label//text()')[0]
	else:
		wnty = 'Not given'
	row.writerow([
		Avail,
		brand,
		category,
		country,
		# discount,
		display,
		ex_date,
		graphics,
		hard_driver,
		momery_card,
		model_name,
		operating_system,
		processer,
		description,
		mrp_price,
		retailer,
		sku_id,
		sales_price,
		battery,
		bluethooth,
		# ctg_links,
		r.url,
		wnty
		])
	print(r.url)

print(url[-1])
for i in url:
	# try:
	n = 0
	while True:
		r = s.get(i.format(n))
		tree = html.fromstring(r.text)
		tr =tree.xpath('//div[@id="pagination" and @class="pagination"]//button[@class="system-result-btn page pagination-btn prev-next-btn"]//@data-disabled')[-1]
		if(tr!='True' and tr):
			lnk = tree.xpath('//h3[@class="ps-title"]//a//@href')
			for j in lnk:
				main_lnk.append(j)
				# cat_lnk.append(r.url)
		else:
			last_link(r)
			# cat_lnk.append(r.url)
			break
		n+=1
		print(r.url)
	# except:
	# 	print('Exception!!!!')
	# 	pass


print(len(main_lnk))
print(len(cat_lnk))
for product_links in main_lnk:
	n = product_links.replace('//www.','https://www.')
	To_data(n)

	# row.writerow([
	# 	n
	# 	])







# def requests_function():
#     for i in n_url:
#         r = s.get(i)
#         tree = html.fromstring(r.text)
#         n = int(''.join(tree.xpath('//button[@class="system-result-btn pagination-btn hide-xs"]//text()')).strip().replace('\n','').split()[-1])
#         return n


# def links_requests(num):
#     for ln in url:
#         for i in range(1,num):
#             r = s.get(ln.format(i))
#             soup = bs(r.content,'html.parser')
#             tree = html.fromstring(r.text)
#             lnk = tree.xpath('//h3//a[@class="dellmetrics-iclickthru"]//@href')
#             if(lnk):
#                 for j in lnk:
#                     # print(j)
#                     nl = j.replace('//www.',"https://www.")
#                     l.append(nl)
#             print(r.url)

# num = requests_function()
# links_requests(num+1)

# for i in l:
#     row.writerow([
#         i
#     ])
