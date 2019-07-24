# -*- coding: utf-8 -*-
import scrapy
from ..items import DictionaryItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://www.english-bangla.com/browse/index/a']

    def parse(self, response):
        get_all_link = response.css('div.a-z>a::attr(href)').extract()
        for letter in get_all_link:
            yield scrapy.Request(url=letter, callback=self.parse_next)

    def parse_next(self, response):
        urls = response.css("div#cat_page>ul>li>a::attr(href)").getall()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)
        next_page_url = response.css('div.pagination>a[rel=next]::attr(href)').extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse_next)

    def parse_details(self, response):
        dictionary = DictionaryItem()
        eng_word = response.css('span#speak.word::text').get().strip()
        bengli_mean = response.css('span.format1::text').get().replace(u'\ax0', u' ').strip()
        dictionary['eng_word'] = eng_word
        dictionary['bengli_mean'] = bengli_mean
        yield dictionary

