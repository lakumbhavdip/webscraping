from requests_html import HTMLSession

url = "https://apps.shopline.com/sort/?type=0&currentPage="

s = HTMLSession()
r =s.get(url)
r.html.render(sleep=1)

apps = r.html.xpath('//*[@class= "_applist_content_warp_1wuz5_1"]')
print(apps)