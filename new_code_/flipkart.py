# -*- coding: utf-8 -*-
import scrapy


class FlipkartSpider(scrapy.Spider):
    name = 'flipkart'
    allowed_domains = ['flipkart.com']
    start_urls = ['http://flipkart.com/']

    def start_requests(self):
        url = 'https://www.flipkart.com/mens-footwear/pr?sid=osp%2Ccil&otracker=nmenu_sub_Men_0_Footwear&page={}'
        for i in range(1,10):
            yield scrapy.Request(url=url.format(i),callback=self.parse)
        
    def parse(self,reponse):
        ln = response.xpath('//div[@class="_1xHGtK _373qXS"]//a/@href').extract()
        for i in ln:
            yield scrapy.Request(url='https://www.flipkart.com'i,callback=self.parse_details)

    def parse_details(self,reponse):
        product_name = response.xpath('//h1[@class="yhB1nd"]//span[@class="B_NuCI"]//text()').get()
        price = response.xpath('//div[@class="_25b18c"]//div[@class="_30jeq3 _16Jk6d"]//text()').get()
        


