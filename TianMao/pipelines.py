# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import TianMao.Common
from scrapy.exceptions import DropItem

import MySQLdb
import MySQLdb.cursors


class DBPipeline(object):
    def __init__(self):
        try:
            self.db = MySQLdb.connect(host="xxx.xxx.xxx.xxx", user="root", passwd="root", port=3306, db="xiaoyusuper",
                                      charset="utf8")
            self.cursor = self.db.cursor()
            print "Connect to db successfully!"
        except:
            print "Fail to connect to db!"

    # pipeline默认调用
    def process_item(self, item, spider):
        if len(item['id']) > 0:
            http = 'http:'
            param = (item['title'][0], http + item['img'][0], item['price'][0], item['price'][0], item['id'][0],
                     http + item['url'][0], TianMao.Common.CURRENT_TYPE,item['valume'][0])
            sql = "insert into goods_info values (%s, %s, %s, %s, %s, %s,%s,%s)"
            self.cursor.execute(sql, param)
            return item
        else:
            return DropItem(item)


class TianmaoPipeline(object):
    def __init__(self):
        self.file = codecs.open('result.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        if len(item['id']) > 0:
            line = json.dumps(dict(item)) + '\n'
            # print line
            self.file.write(line.decode("unicode_escape"))
            return item
        else:
            return DropItem('id is null')