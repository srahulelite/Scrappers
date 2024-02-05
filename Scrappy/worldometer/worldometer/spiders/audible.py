import scrapy

class AudibleSpider(scrapy.Spider):
    name = "audible"
    allowed_domains = ["www.audible.com"]
    start_urls = ["https://www.audible.com/search"]

    def parse(self, response):
        product_container = response.xpath('//div[@class="adbl-impression-container "]/div/span/ul/li')
        
        for product in product_container:
            title = product.xpath('.//h3[contains(@class,"bc-heading")]/a/text()').get()

            yield{
                'title':title
            }
        pagination = response.xpath('//ul[contains(@class,"pagingElements")]')
        next_page_url = pagination.xpath('.//span[contains(@class,"nextButton")]/a/@href').get()

        if(next_page_url):
            yield response.follow(url=next_page_url, callback=self.parse)
