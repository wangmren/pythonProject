# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter


class MaoyanThreadPipeline:
    def open_spider(self,spider):
        print('我是open_spider的函数输出')
        #一般用于建立数据库的链接
        self.db=pymysql.connect(
            # 数据库地址
                    host='127.0.0.1',
                    # 数据库端口
                    port=3306,
                    # 数据库名
                    db='Maoyan',
                    # 数据库用户名
                    user='root',
                    # 数据库密码
                    passwd='123456',
                    # 编码方式
                    charset='utf8',
                    use_unicode=True
        )
        self.cursor=self.db.cursor()

    #爬虫项目结束时运行的函数
    def close_spider(self, spider):
        print('我是close_spider函数的输出')
        # 用于断开数据库的链接
        self.cursor.close()
        self.db.close()
    def process_item(self, item, spider):
        print(item['name'], item['star'], item['time'])
        return item
