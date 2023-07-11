import scrapy
from ..items import MaoyanItem

class MaoyanSpider(scrapy.Spider):
    name = "maoyan"
    allowed_domains = ["maoyan.com"]
    start_urls = ["https://maoyan.com/board/4?offset=0"]

    def parse(self, response):
        print(response)
#         创建基础对象
        item = MaoyanItem()

        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')

        for dd in dd_list:
            item['name'] = dd.xpath('./a/@title').get().strip()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').get().strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').get().strip()[5:15]
            yield item