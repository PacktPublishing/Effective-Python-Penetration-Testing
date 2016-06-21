# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
from pprint import pprint
from testSpider.items import TestspiderItem

class PactpubSpider(Spider):
    name = "pactpub"
    allowed_domains = ["pactpub.com"]
    start_urls = (
        'https://www.pactpub.com/all',
    )

    def parse(self, response):
	res = Selector(response)
	items = []
        for sel in res.xpath('//div[@class="book-block"]'):
            item = TestspiderItem()

            item['book'] = sel.xpath('//div[@class="book-block-title"]/text()').extract()
	    items.append(item)
	return items

