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
            # 注意:item中的key的名字一定要跟items.py中的命名一致
            item['name'] = dd.xpath('./a/@title').get().strip()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').get().strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').get().strip()[5:15]
            # 利用生成器 把item放到管道文件中
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
