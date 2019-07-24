# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DictionaryItem(scrapy.Item):
    # define the fields for your item here like:
    eng_word = scrapy.Field()
    bengli_mean = scrapy.Field()

    pass
