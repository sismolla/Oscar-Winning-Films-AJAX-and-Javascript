import scrapy
import json
from ajax_scraper.items import AjaxScraperItem

class AjaxsxraperSpider(scrapy.Spider):
    name = "ajaxsxraper"
    allowed_domains = ["www.scrapethissite.com"]
    start_urls = ["https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2010",
                  "https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2011",
                  "https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2012",
                  "https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2013",
                  "https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2014",
                  "https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2015",
                  ]

    def parse(self, response):
        yield scrapy.Request(response.url, callback=self.parse)

    def parse(self, response):
        yield scrapy.Request(
            url=response.url,
            callback=self.parser_func            
        )

    def parser_func(self, response):
        item = AjaxScraperItem()
        raw_data = response.body
        json_data = json.loads(raw_data)
        for data in json_data:
            item["title"] =  data["title"]
            item["year"] =  data["year"]
            item["awards"] = data["awards"]
            item["nominations"] = data["nominations"]
            
            yield item