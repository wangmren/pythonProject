import scrapy

from ..items import Maoyan2Item


class Maoyan2Spider(scrapy.Spider):
    name = "maoyan2"
    allowed_domains = ["maoyan.com"]
    start_urls = ["https://maoyan.com/board/4?offset=0"]
    offset = 0


    def parse(self, response):
        print(response)  # 为了防止校验

        # 加载items对象
        item = Maoyan2Item()
        # 基础的xpath
        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        # 依次遍历
        for dd in dd_list:
            item['name'] = dd.xpath('./a/@title').get().strip()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').get().strip()
            # item['time'] =dd.xpath('.//p[@class="releasetime"]/text()').get().strip()
            time = dd.xpath('.//p[@class="releasetime"]/text()').get().strip()[5:].split('(')[0]
            # item['time']=(len(time)<10 and time+'-01' or time)#三目的写法 只能添加一个 - 01
            item['time'] = self.zhengli(time)
            yield item
        self.offset += 10
        if self.offset <= 91:
            url = 'https://maoyan.com/board/4?offset={}'.format(self.offset)
        # 交给调度器进入队列
            yield scrapy.Request(
                url=url,
                # 指定解析函数对象
                callback=self.parse
            )


    def zhengli(self, time):
        if len(time) < 10:
            time = time + '-01'
            time = self.zhengli(time)
        return time
