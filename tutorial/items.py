# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#中文支持吗
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    