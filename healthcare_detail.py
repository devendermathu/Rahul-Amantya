from requests import Session
from lxml import html
import json
import re
import csv
from bs4 import BeautifulSoup as bs
s = Session()
s.headers['User-Agent']="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"
f = open('healthcare_Links_file.txt','r').read().split('\n')
fw = open('healthcare_details_page.csv','w',encoding="utf-8",newline="")
row = csv.writer(fw)
for i in f[:10]:
	r = s.get(i)
	tree = html.fromstring(r.text)
	soup = bs(r.content,'html.parser')
	title = ''.join(tree.xpath('//h1//text()')).strip()
	short_description = ''.join(tree.xpath('//div[@class="product-download"]//text()')).strip()
	# long_descriptions = ''.join(tree.xpath('//div[@class="field--label" and contains(string(),"Features")]//following-sibling::div//div[@class="paragraph paragraph--type--bp-simple paragraph--view-mode--default paragraph--id--705"]//text()')).strip().replace('\n','') + ''.join(tree.xpath('//div[@class="field--label" and contains(string(),"Features")]//following-sibling::div//div[@class="paragraph paragraph--type--bp-columnsparagraph--view-mode--default paragraph--id--708"]//text()')).strip().replace('\n','') + ''.join(tree.xpath('//div[@class="field--label" and contains(string(),"Features")]//following-sibling::div//div[@class="paragraph paragraph--type--bp-columnsparagraph--view-mode--default paragraph--id--711"]//text()')).strip().replace('\n','')
	long_descriptions = ''.join(tree.xpath('//div[@class="field--label" and contains(string(),"Features")]//following-sibling::div//div[@class="paragraph__column"]//text()')).strip().replace('\n','')
	print(long_descriptions)
	pdf_link = '|'.join(tree.xpath('//a[@class="content"]//@href'))
	row.writerow([
		'stanleyhealthcare',
		r.url,
		title,
		short_description,
		long_descriptions,
		pdf_link
		])
	print()