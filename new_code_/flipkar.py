import scrapy


class FlipkarSpider(scrapy.Spider):
    name = 'flipkar'
    allowed_domains = ['flipkart.com']
    start_urls = ['http://flipkart.com/']

    def start_requests(self):
        url = "https://www.flipkart.com/mens-footwear/sports-shoes/pr?sid=osp%2Ccil%2C1cu&otracker=nmenu_sub_Men_0_Sports+Shoes&page={}"
        for i in range(1,10):
            yield scrapy.Request(url=url.format(i),method="GET",callback=self.parse)
    
    def parse(self,response):
        ul = response.xpath('//a[@class="IRpwTa"]//@href').getall()
        for i in ul:
            yield scrapy.Request(url='https://www.flipkart.com'+i,callback=self.parse_data)
    def parse_data(self,response):
        yield{
            'URL':response.url,
            'Product name':response.xpath('//span[@class="B_NuCI"]//text()').get(),
            'Price':response.xpath('//div[@class="_30jeq3 _16Jk6d"]//text()').get(),
            'Discount On':''.join(response.xpath('//div[@class="_3Ay6Sb _31Dcoz pZkvcx"]//span//text()').get()).replace("""% off""",''),
            'Brand':''.join(response.xpath('//span[@class="G6XhRU"]//text()').get()).replace('\xa0',''),
            'Ratings':response.xpath('//span[@class="_2_R_DZ"]//text()').get(),
            'Type of shows':response.xpath('//div[@class="col col-3-12 _2H87wv" and contains(string(),"Occasion")]//following-sibling::div//text()').get(),
            'Model name':response.xpath('//div[@class="col col-3-12 _2H87wv" and contains(string(),"Model Name")]//following-sibling::div//text()').get(),
            'sole':response.xpath('//div[@class="col col-3-12 _2H87wv" and contains(string(),"Sole Material")]//following-sibling::div//text()').get(),
            'color':response.xpath('//div[@class="col col-3-12 _2H87wv" and contains(string(),"Color")]//following-sibling::div//text()').get(),
            'Ideal For':response.xpath('//div[@class="col col-3-12 _2H87wv" and contains(string(),"Ideal For")]//following-sibling::div//text()').get(),
            'top':response.xpath('//div[@class="col col-3-12 _2H87wv" and contains(string(),"Leather Type")]//following-sibling::div//text()').get(),
            'breadcumps':'->'.join(response.xpath('//div[@class="_1MR4o5"]//div//a//text()').getall())
        }