import scrapy

class WorldometerSpider (scrapy.Spider):
    name = "worldometer"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    def parse (self, response) :
        # title = response.xpath('//hl/text ()').get()
        countries = response.xpath('//td/a') 
        countrydic = {}
        for country in countries:
            link = country.xpath ('.//@href').get()
            countrydic[country.xpath('.//text()').get()] = link

            #absolutepath
            #absolute_path = f"https://www.worldometers.info/{link}"
            #absolute path response.urljoin (link)
            yield response.follow (url=link, callback=self.parseCountry)


    def parseCountry (self, response) :
        rows = response.xpath ("//table [contains (@class, 'table')] [1]/tbody/tr")
        #Population of <INDIA> (2024 and historical)
        country = response.xpath ("//h2 [1]/text()").get ().split() [2]
        perYearCalc = {}
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            perYearCalc[year] = population
            perYearCalc['country'] = country

        yield perYearCalc