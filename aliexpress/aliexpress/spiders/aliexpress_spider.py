# import scrapy
from ..items import AliexpressItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AliexpressTest(CrawlSpider):
    name = 'aliexpress_spider'
    allowed_domains = ['www.aliexpress.com']
    start_urls = ['https://www.aliexpress.com/sitemap.html']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        name = response.xpath('//h1[@class="product-name"]/text()').extract_first()
        orders = response.xpath('//span[@class="order-num"]/text()').re_first(r"(\d+)")
        url = response.url

        fields = AliexpressItem(name=name, orders=orders, url=url)

        yield fields