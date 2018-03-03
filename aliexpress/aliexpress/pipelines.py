# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import sqlite3

# class AliexpressPipeline(object):
#     def process_item(self, item, spider):
#         return item


class NotNone(object):
    def process_item(self, item, spider):
        if item['name'] is not None:
            return item
        else:
            raise DropItem("There is no data on this page %s" % item)


class InsertIntoDB(object):
    def process_item(self, item, spider):
        item['id'] = item['id']
        item['name'] = item['name']
        item['orders'] = item['orders']
        item['url'] = item['url']

        conn = sqlite3.connect('aliexpress_db.sqlite')
        c = conn.cursor()

        c.execute("INSERT INTO products (id, name, orders, url) VALUES (?, ?, ?, ?)", (item['id'], item['name'], item['orders'], item['url'],))
        conn.commit()
        conn.close()

        return item