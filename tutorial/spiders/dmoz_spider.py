#coding=utf-8
import scrapy
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["w3school.com.cn"]
    start_urls = [
        "http://www.w3school.com.cn/xpath/xpath_syntax.asp"
    ]

    def parse(self, response):
        items = []
        for sel in response.xpath('//div[@id="course"]/ul[1]/li'):
            #title = sel.xpath('a/text()').extract()
            #link = sel.xpath('a/@href').extract()
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            items.append(item)
        return items
        #, desc
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)