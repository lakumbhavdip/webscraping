import scrapy
from scrapy_selenium import SeleniumRequest

class ScrapSpiderSpider(scrapy.Spider):
    name = "scrap_spider"
    allowed_domains = ["apps.shopline.com"]
    # start_urls = ["https://apps.shopline.com/sort/?type=0"]

    def start_requests(self):
        yield SeleniumRequest(
            url="https://apps.shopline.com/sort/?type=0&currentPage=",
            callback=self.parse,
        )
        
    def parse(self, response):
        for element in response.selector.xpath("//div[@class='_description_warp_1wuz5_45']"):
            appname = element.xpath('./h4/title_3 color_black1 _appName_warp_1wuz5_34()').extract_first()
            yield{
                "AppName": appname 
            }