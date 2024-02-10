import scrapy
from ..pipelines import OfficescrappersPipeline

class TechcrunchSpider(scrapy.Spider):
    name = "techcrunch"
    allowed_domains = ["techcrunch.com", "feeds.a.dj.com"]
    start_urls = ["https://techcrunch.com/category/fintech/feed/"]


    def start_requests(self):
        urls = [
            "https://techcrunch.com/category/fintech/feed/",
            "https://feeds.a.dj.com/rss/RSSWSJD.xml"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        OfficescrappersPipeline.output_ready()
        
    def parse(self, response):
        for post in response.xpath('//channel/item'):
            yield {
                'origin' : response.xpath("//channel/title/text()").extract_first(),
                'title' : post.xpath('title//text()').extract_first(),
                'link': post.xpath('link//text()').extract_first(),
                'pubDate' : post.xpath('pubDate//text()').extract_first(),
                'description' : post.xpath('description//text()').extract_first(),
            }
        
        

    
