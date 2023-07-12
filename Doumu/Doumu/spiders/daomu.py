import scrapy
from ..items import DoumuItem

class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ["www.beqege.com"]
    # start_urls = ['http://www.daomubiji.com/']
    start_urls=["https://www.beqege.com/class1/"]

    def parse(self, response):
        item = DoumuItem()
        item['title']=response.xpath('//*[@id="wrapper"]/div[3]/ul/li[2]/a/text()').get()
        #基础地址
        two_url='https://www.beqege.com'+response.xpath('//*[@id="hotcontent"]/div/div[1]/dl/dt/a/@href').get()
        yield scrapy.Request(
            url=two_url,
            meta={'item':item},
            callback=self.parse_two_page
        )
        #二级页面
    def parse_two_page(self,response):
        item=response.meta['item']
        print(item,response)
        dd_list=response.xpath('//*[@id="list"]/dl/dd[1]')
        for dd in dd_list:
            name=dd.xpath('./a/text()').get()
            san_link='https://www.beqege.com'+dd.xpath('./a/@href').get()
            yield scrapy.Request(
                url=san_link,
                meta={'item':item,'name':name},
                callback=self.parse_san_page
            )
            break
    #三级
    def parse_san_page(self,response):
        item=response.meta['item']
        item['name']=response.meta['name']
        neirong_list=response.xpath('//*[@id="content"]/text()').extract()
        neirong_list.insert(0,item['name'])
        content='\n'.join(neirong_list)
        item['content']=content
        yield item
