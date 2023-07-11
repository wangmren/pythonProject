# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanMysqlPipeline:
    def process_item(self, item, spider):
        return item

import pymysql
from .settings import *
class Maoyan_MysqlPipenline(object):
    #爬虫项目开始时运行的函数
    def open_spider(self,spider):
        print('我是open_spider的函数输出')
        #一般用于建立数据库的链接
        self.db=pymysql.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PWD,
            database=MYSQL_DB,
            charset=MYSQL_CHAR
        )
        self.cursor=self.db.cursor()
        #爬虫项目结束时运行的函数
    def close_spider(self,spider):
        print('我是close_spider函数的输出')
        #用于断开数据库的链接
        self.cursor.close()
        self.db.close()
        #爬虫管道类必须要有的函数
    def process_item(self,item,spider):
        ins='insert into maoyantab values(%s,%s,%s)'
        L=[item['name'],item['star'],item['time']]
        self.cursor.execute(ins,L)
        self.db.commit()
        #一定要有 返回item的语句!!!!!!!!!
        return item
