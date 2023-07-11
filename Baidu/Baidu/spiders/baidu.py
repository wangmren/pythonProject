import scrapy


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["www.baidu.com"]
    start_urls = ["https://www.baidu.com"]

    def parse(self, response):
        # result = response.xpath('/html/head/title/text()')[0]
        result = response.xpath('/html/head/title/text()').get()
        print('*'*50)
        print(result)
        print('*'*50)
