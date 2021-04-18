from requests import Session
from lxml import html
import re
import csv
from bs4 import BeautifulSoup as bs
fr = open('readfile.txt','r').read().split('\n')
fw = open('outputfile.csv','w',encoding='utf-8',newline="")
row = csv.writer(fw)
s = Session()
s.headers['User-Agent']="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"
for i in fr:
	r = s.get(i)
	soup = bs(r.content,"html.parser")
	tree = html.fromstring(r.text)
	compatitor_price =  ''.join(tree.xpath('//div[@id="product_detail_price"]//span[@class="product-price__regular js-product-price"]//text()')).strip().replace(' €','')
	competitor_markdown_price=''
	compatitor_id = ''.join(tree.xpath('//table[@class="properties_table"]//tr//td//div[contains(string(),"Herstellernummer:")]//ancestor::td//following-sibling::td//text()')).strip()
	product_name = ''.join(tree.xpath('//h1[@class="name squeezed"]//text()')).strip()
	competitor_model=''
	display_size = ''.join(tree.xpath('//tr//td[@class="produktDetails_eigenschaft2" and contains(string(),"Displaygröße")]//following-sibling::td//text()'))
	os_type =  ''.join(tree.xpath('//tr//td[@class="produktDetails_eigenschaft2" and contains(string(),"Betriebssystem")]//following-sibling::td//text()'))
	processer = ''.join(tree.xpath('//img[@class="pdp-properties-processor-logo"]//ancestor::td//ancestor::tr//td[@width="500"]//text()'))
	competitor_processor_model = ''
	graphics = ''.join(tree.xpath('//td[@class="produktDetails_eigenschaft2" and contains(string(),"Grafikkarte")]//following-sibling::td//text()'))
	hard_disk = ''.join(tree.xpath('//td[@class="produktDetails_eigenschaft2" and contains(string(),"Kapazität (Gesamt)")]//following-sibling::td//text()'))
	ram = ''.join(tree.xpath('//td[@class="produktDetails_eigenschaft2" and contains(string(),"Größe")]//following-sibling::td//text()'))
	resolution = ''.join(tree.xpath('//td[@class="produktDetails_eigenschaft2" and contains(string(),"Auflösung")]//following-sibling::td//text()'))
	backlight =  ''.join(tree.xpath('//td[@class="produktDetails_eigenschaft2" and contains(string(),"Tastaturbeleuchtung")]//following-sibling::td//text()'))
	competitor_optical_drive=""
	competitor_warranty=""
	seller_name=""
	stock=""
	row.writerow([
		compatitor_price,
		competitor_markdown_price,
		compatitor_id,
		product_name,
		competitor_model,
		r.url,
		display_size,
		os_type,
		processer,
		competitor_processor_model,
		graphics,
		hard_disk,
		ram,
		resolution,
		backlight,
		competitor_optical_drive,
		competitor_warranty,
		seller_name
		])
	print(r.url)