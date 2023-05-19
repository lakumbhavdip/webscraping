from bs4 import BeautifulSoup
from urllib.request import urlopen

urls = []
url = 'https://www.waleedtoys.com/BrandList?cid=Ki3bgiSxO3vQ6MnH4WXcXXSbegSfsseiyny0'
file = urlopen(url)
html = file.read()
soup = BeautifulSoup(html, "html.parser")

apps = soup.select("div.row.product-listing div.col-lg-3.col-md-3.col-sm-6.product-column div.product-th div.product-card").find_all("a", href=True)

if apps:
    urls.append(apps['href'])
print(apps)
print(urls)

# # if first_anchor:
# #     urls.append(first_anchor['href'])
# app = apps.find("a", href=True)
# print(app)
# print(len(urls))

# anchors =soup.body.find("div",{"class":"more-cart"}).find("a", href=True)
# for anchor in anchors:
#     print(anchor['href'])