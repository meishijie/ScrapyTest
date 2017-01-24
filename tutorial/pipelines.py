# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs

class TutorialPipeline(object):

    def __init__(self):
        #字符编码encoding='GBK'  encoding='utf-8'
        self.file = codecs.open('items.csv', 'w', encoding='GBK')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        print line
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()



