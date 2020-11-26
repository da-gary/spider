# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class YgSpider(CrawlSpider):
    name = 'yg'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'wz.sun0769.com/political/index/politicsNewest?id=1&page=\d+'), follow=True),

        Rule(LinkExtractor(allow=r'/political/politics/index?id=\d+'), callback='parse_item'),
    )

    def parse(self, response):
        item = {}
        # item['content'] = response.xpath('//span/a/@href').get()
        print(response.text)

