import scrapy
import csv


# class QuoteSpider(scrapy.Spider):
#     name = "quotes"
#     start_urls = [
#     # 'https://ecosystem.hubspot.com/marketplace/apps/marketing/social-media/vidmob'
#     'https://www.hubspot.com/company/contact'
#     ]

#     # def parse(self, response):
#     # contryname = response.css('h5.hsg-multi-col__name::text').extract ()
#     # phoneNumber = response.css('p.hsg-multi-col__description,a::text')
#     # yield {'contryname': contryname , 'phonenumber':phoneNumber}
#     def parse(self, response):
#         address = response.css('p+ p::text').extract()
#         city = response.css('.hsg-multi-col__name::text').extract()
#         phone = response.css('.hsg-multi-col__description::text').extract()
#         yield {"Address":address,"city":city,"phone number ":phone}

# class AppSpider(scrapy.Spider):
#     name = "app_spider"
#     start_urls = ["https://apps.shopline.com/detail/?appHandle=zhekouhuodongsh"]

#     def parse(self, response):
#         app_title = response.css("h1.detail--apps--title::text").get()
#         developer_name = response.css("a.apps--card--developer-name::text").get()
#         yield {
#             "App Title": app_title,
#             "Developer Name": developer_name,
#         }

# class AppSpider(scrapy.Spider):
#     name = "app_name"
#     url = ["https://apps.shopline.com/sort/?type=0&currentPage="]
    
#     def appscrap(self,response):
#         appname = response.css("._appName_warp_1wuz5_34::text").extract()
#         yield appname

class BlogSpider(scrapy.Spider):
    name = "toys"
    url = ["https://www.waleedtoys.com/BrandList?cid=Ki3bgiSxO3vQ6MnH4WXcXXSbegSfsseiyny0"]
    
    def blogscrap(self,response):
        bloghead = response.css('div.view-more-div a(attr)::text').get()
        print(bloghead)
        # yield bloghead