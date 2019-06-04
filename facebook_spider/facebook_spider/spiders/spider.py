# -*- coding: utf-8 -*-
import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['https://www.facebook.com/']
    start_urls = ['http://https://www.facebook.com//']

    def parse(self, response):
        pass
