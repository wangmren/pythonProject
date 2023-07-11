import scrapy


class MaoyanSpider(scrapy.Spider):
    name = "maoyan"
    allowed_domains = ["maoyan.com"]
    start_urls = ["https://maoyan.com"]

    def parse(self, response):
        pass
