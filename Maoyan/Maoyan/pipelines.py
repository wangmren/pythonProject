# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
import pymysql


class MaoyanPipeline:
    def __init__(self):
        self.connect = pymysql.connect(
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
            use_unicode=True)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        print(item['name'], item['star'], item['time'])
        self.cursor.execute(
            """insert into jiben(name, star,time) value (%s, %s, %s)""",  # 纯属python操作mysql知识，不熟悉请恶补
            (item['name'],  # item里面定义的字段和表字段对应
             item['star'],
             item['time'],))

        # 提交sql语句
        self.connect.commit()

        return item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.connect.close()


