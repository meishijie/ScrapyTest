#coding=utf-8
import scrapy
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "cnbeta"
    allowed_domains = ["cnbeta.com"]
    start_urls = [
        "http://www.cnbeta.com/"
    ]

    def parse(self, response):
        items = []
        for sel in response.xpath('//*[@id="hot"]/dl'):
            #title = sel.xpath('a/text()').extract()
            #link = sel.xpath('a/@href').extract()
            item = DmozItem()
            item['title'] = sel.xpath('dt/a/text()').extract()
            item['link'] = sel.xpath('dt/a/@href').extract()
            item['image_urls']=sel.xpath('dd/div/a/img/@src').extract()
            items.append(item)
        return items
        #, desc
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)