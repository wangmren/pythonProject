import scrapy


class MaoyanMysqlSpider(scrapy.Spider):
    name = "maoyan_mysql"
    allowed_domains = ["maoyan.com"]
    start_urls = ["https://maoyan.com"]

    def parse(self, response):
        pass
