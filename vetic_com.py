from lxml import html
from requests import Session
from bs4 import BoutifulSoup as BS
import re
import csv
url = 'https://www.vertiv.com/api-lang/en-CA/SearchProductTypeResults/search'
f = open('vetic_come.txt','r').read().split('\n')
data = {'facetGroups':[],'pageNumber':'{}','pageSize':'10','productTypeId':'{}'}
fw = open('outputfile.txt','w',encoding="utf-8")
for i in range(1,3):
	data.update({'pageNumber':'{}'.format(i)})
	for j in f[5]:
		data.update({'productTypeId':'{}'.format(j)})
		r = s.post(url,data)
		