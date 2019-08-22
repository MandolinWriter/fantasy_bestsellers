# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Top100ScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class BookItem(scrapy.Item):
    f_rank = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    price = scrapy.Field()
    ku = scrapy.Field()
    series = scrapy.Field()
    series_num = scrapy.Field()
    series_len = scrapy.Field()
    blurb = scrapy.Field()
    rating = scrapy.Field()
    review_count = scrapy.Field()
    all_rank = scrapy.Field()
    page_count = scrapy.Field()
    publisher = scrapy.Field()
