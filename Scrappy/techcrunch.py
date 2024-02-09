import scrapy


class TechcrunchSpider(scrapy.Spider):
    name = "techcrunch"
    allowed_domains = ["legal.yahoo.com"]
    start_urls = ["https://legal.yahoo.com/us/en/yahoo/terms/otos/index.html"]

    def parse(self, response):
        pass
