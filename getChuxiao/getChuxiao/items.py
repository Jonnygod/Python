# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GetchuxiaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Gname = scrapy.Field()
    cost = scrapy.Field()
    price = scrapy.Field()
    grade = scrapy.Field()
    
