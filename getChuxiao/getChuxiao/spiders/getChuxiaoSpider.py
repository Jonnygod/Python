# -*- coding: utf-8 -*-
import scrapy
from getChuxiao.items import GetchuxiaoItem
import time




class GetchuxiaospiderSpider(scrapy.Spider):
    name = 'getChuxiaoSpider'
    allowed_domains = ['xiaoheihe.cn']
    baseurl='https://www.xiaoheihe.cn/games/index'
    start_urls = []
    # start_urls.append(baseurl)
    page = int(input("输入："))
    for i in range(1,page+1):
        start_urls.append(baseurl)


    def parse(self, response):
        selector1 = response.xpath('//li[@data-v-68ed2416=""]')
        items = []
        for selector in selector1:
            item = GetchuxiaoItem()
            item['Gname'] = selector.xpath('.//div[@class="info-wrapper"]/h3/text()').extract()[0]
            item['cost'] = selector.xpath('.//span[@class="discount"]/text()').extract()[0]
            item['price'] = selector.xpath('.//span[@class="p"]/text()').extract()[0]
            item['grade'] = selector.xpath('.//p[@class="score-wrapper size-large color-1"]/span[2]/text() | .//p[@class="score-wrapper size-large color-2"]/span[2]/text() | .//p[@class="score-wrapper size-large color-3"]/span[2]/text() | .//span[@class="less"]/text() | .//p[@class="score-wrapper size-large color-4"]/span[2]/text()').extract()[0]
            items.append(item)
        return items

