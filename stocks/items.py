# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StocksItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    symbol = scrapy.Field()
    analysts = scrapy.Field()
    median = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
    increase = scrapy.Field()
    last_price = scrapy.Field()
    pass
