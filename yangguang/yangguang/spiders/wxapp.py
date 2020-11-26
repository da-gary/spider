# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from yangguang.items import WxappItem

class WxappSpider(CrawlSpider):
    name = 'wxapp'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php']

    rules = (
        # 列表页面
        Rule(LinkExtractor(allow=r'www.wxapp-union.com/portal.php?mod=list&catid=1&page=\d+'), follow=True),
        # 详情页面
        Rule(LinkExtractor(allow=r'article-\d+-1.html'), callback='parse_item'),

    )

    def parse_item(self, response):
        item = WxappItem()
        item['title'] = response.xpath('//h1/text()').get()
        item['author'] = response.xpath('//p[@class="authors"]/a/text()').get()
        item['pub_date'] = response.xpath('//p[@class="authors"]/span/text()').get()

        yield item
