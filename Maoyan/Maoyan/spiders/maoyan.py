import scrapy


class MaoyanSpider(scrapy.Spider):
    name = "maoyan"
    allowed_domains = ["maoyan.com"]
    start_urls = ["https://maoyan.com"]

    def parse(self, response):
        # result = response.xpath('/html/head/title/text()')[0]
        result = response.xpath('/html/head/title/text()').get()
        print('*' * 50)
        print(result)
        print('*' * 50)

