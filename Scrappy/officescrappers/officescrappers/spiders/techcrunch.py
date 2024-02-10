import scrapy


class TechcrunchSpider(scrapy.Spider):
    name = "techcrunch"
    allowed_domains = ["wsj.com"]
    start_urls = ["https://wsj.com/tech"]

    def parse(self, response):
        front_news = response.xpath("//div[contains(@data-testid,'allesseh')]")
        categorized_news = response.xpath("//div[@class ='css-1qsgmm']")
        
        for news_category in categorized_news:
            category = news_category.xpath(".//h2[contains(@class,'eoniv5f2')]/text()").get()

            yield{
                'category': category
            }

