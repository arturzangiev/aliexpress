# -*- coding: utf-8 -*-
import scrapy
from ..items import AliexpressItem

class AliexpressSpiderSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["aliexpress.com"]
    start_urls = ['https://www.aliexpress.com/w/wholesale-fingers-print.html?spm=2114.11147653.3030.25.57612e5cSSxomP']

    def parse(self, response):

        name = response.xpath('//h1[@class="product-name"]/text()').extract_first()
        orders = response.xpath('//span[@class="order-num"]/text()').re_first(r"(\d+)")
        url = response.url

        fields = AliexpressItem(name=name, orders=orders, url=url)

        yield fields