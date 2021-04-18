import scrapy
import re

class A11stSpider(scrapy.Spider):
    name = '11st'
    allowed_domains = ['11st.co']
    start_urls = ['http://11st.co/']

    def start_requests(self):
        url = 'http://www.11st.co.kr/products/2770861622?trTypeCd=21&trCtgrNo=1002946'
        yield scrapy.Request(url=url,method="GET",callback=self.parse)
    
    def parse(self,response):
        yield{
            'product name': ''.join(response.xpath('//h1[@class="title"]//text()')).strip(),
            'Brand name':''.join(response.xpath('//h1[@class="title"]//text()')).split()[0],
            'mark_markdown price': ''.join(response.xpath('//dl[@class="price_regular"]//dd//span[@class="value"]//text()')).strip(),
            'product price':''.join(response.xpath('//ul[@class="price_wrap"]//li//dl//dd//strong//span[@class="value"]//text()')).strip(),
            'discount':re.search(' <dd><span class="value">(.*?)</span><span class="unit">%</span></dd>',response.text).group(1),
            'processor_brand':'',
            'processor gen':'',
            'product img':''.join(response.xpath('//div[@class="img_full"]//img//@src')),
            'product reviews': 'Product review '+''.join(+re.search('id="tabMenuDetail2">상품리뷰 <i>(.*?)</i></button>',response.text).group(1))
            'seller name':''.join(response.xpath('''//table[@class="prdc_detail_table"]//tr//th[contains(string(),"판매자명")]//following-sibling::td//text()'''))
            }