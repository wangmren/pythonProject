import scrapy


class Maoyan2Spider(scrapy.Spider):
    name = "maoyan2"
    allowed_domains = ["maoyan.com"]
    start_urls = ["https://maoyan.com"]

    def parse(self, response):
        pass
