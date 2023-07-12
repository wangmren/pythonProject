import scrapy
from ..items import MaoyanThreadItem

class MaoyanThreadSpider(scrapy.Spider):
    name = 'maoyan_thread'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']
    #重写父类的方法
    def start_requests(self):
        for offset in range(0,91,10):
            url='https://www.maoyan.com/board/4?timeStamp=1638962905523&channelId=40011&index=1&signKey=cb357464ef369578b9d3d41970526d35&sVersion=1&webdriver=false&offset={}'.format(offset)
            #交给调度器入队列
            yield scrapy.Request(url=url,callback=self.parse)
        #解析
    def parse(self, response):
        print(response)
        #加载items对象
        item=MaoyanThreadItem()
        #获取基准xpath
        dd_list=response.xpath('//dl[@class="board-wrapper"]/dd')
        #遍历list 解析
        for dd in dd_list:
            item['name'] = dd.xpath('./a/@title').get().strip()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').get().strip()
            # item['time'] =dd.xpath('.//p[@class="releasetime"]/text()').get().strip()
            time = dd.xpath('.//p[@class="releasetime"]/text()').get().strip()[5:].split('(')[0]
            # item['time']=(len(time)<10 and time+'-01' or time)#三目的写法 只能添加一个 - 01
            item['time'] = self.zhengli(time)
            yield item

    def zhengli(self, time):
        if len(time) < 10:
            time = time + '-01'
            time = self.zhengli(time)
        return time
