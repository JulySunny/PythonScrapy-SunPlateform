# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Suncrawl1Item(scrapy.Item):
    # define the fields for your item here like: 定义item字段,通过scrapy.Field()去定义
    # name = scrapy.Field()
    type = scrapy.Field()
    title = scrapy.Field()
    # 详情的链接
    href = scrapy.Field()
    # 状态
    state = scrapy.Field()
    # 网友
    person = scrapy.Field()
    content = scrapy.Field()
    content_img = scrapy.Field()
    publish_date = scrapy.Field()
