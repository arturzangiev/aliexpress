# -*- coding: utf-8 -*-
import scrapy
from ..items import AliexpressItem


class AliExpressPopular(scrapy.Spider):
    name = "aliexpress_popular"
    allowed_domains = ["aliexpress.com"]
    start_urls = ['https://www.aliexpress.com/popular.html']

    def parse(self, response):
        urls = response.xpath('//ul/li/span/a/@href').extract()
        for url in urls:
            yield scrapy.Request(url, callback=self.individual_page)

    def individual_page(self, response):
        box = response.xpath('//div[@class="item"]')
        id = box.xpath('.//div[@class="add-to-wishlist"]/a/@data-product-id').extract_first()
        name = box.xpath('.//h3/a/@title').extract_first()
        orders = box.xpath('.//div[@class="rate-history"]/span[@class="order-num"]/a/em/text()').re_first(r"(\d+)")
        url = box.xpath('.//h3/a/@href').extract_first()
        full_url = "https:" + url

        fields = AliexpressItem(id=id, name=name, orders=orders, url=full_url)

        yield fields

        # Calling next page
        next_page_url = response.xpath('//a[@class="page-next ui-pagination-next"]/@href').extract_first()
        next_page_full_url = "https:" + next_page_url
        yield scrapy.Request(next_page_full_url, callback=self.individual_page)