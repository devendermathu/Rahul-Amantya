from requests import Session
from lxml import html
import json
import re
s = Session()
s.headers['User-Agent']="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"
f = open('healthcare_Links_file.txt','w',encoding="utf-8")
data = {
	'view_name':'products',
	"view_display_id":"page_1",
	"view_args":"",
	'view_path':"/products",
	"view_base_path":"products",
	'view_dom_id':'f95accdc074cf1a1b27a8327824d27ff37475f3d46c8d2fc67ca48f1b0a3c94d',
	'pager_element':'0',
	'page':"",
	'_drupal_ajax':"1",
	'ajax_page_state[theme]':"stanley_bootstrap",
	'ajax_page_state[theme_token]':'',
	'ajax_page_state[libraries]':'addtoany/addtoany,better_exposed_filters/auto_submit,better_exposed_filters/general,blazy/load,bootstrap/popover,bootstrap/tooltip,bootstrap_site_alert/dismissed-cookie,core/html5shiv,datalayer/behaviors,facets/drupal.facets.hierarchical,facets/drupal.facets.link-widget,search_api_autocomplete/search_api_autocomplete,stanley_bootstrap/product_slider,system/base,views/views.module,views_infinite_scroll/views-infinite-scroll,views_infinite_scroll/views-infinite-scroll-behaviors,waypoints/waypoints'
}
url = "https://www.stanleyhealthcare.com/views/ajax?_wrapper_format=drupal_ajax"

for i in range(1,50):
	data.update({'page':i})
	# print(i)
	r = s.post(url,data=data)
	if(r.status_code==200):
		js = json.loads(r.text)
		lnk = re.findall('<a href="(.*?)"',js[1]['data'])
		for j in lnk:
			f.write(j+'\n')
	else:
		break
	print(r.url)
	print(i)



# tr = True
# while True:
# 	n = 1
# 	n+=1
# 	print(n)
# 	if(tr==True):
# 		data.update({'page':'{}'.format(n)})
# 		r = s.post(url,data=data)
# 		if(r.status_code==200):
# 			js = json.loads(r.text)
# 			lnk = re.findall('<a href="(.*?)"',js[1]['data'])
# 			for j in lnk:
# 				f.write(j+'\n')

# 			# lnk = re.findall()js[1]['data']
# 		else:
# 			tr = False
# 			break
# 	else:
# 		break
	# n+=1
	# print(n)

