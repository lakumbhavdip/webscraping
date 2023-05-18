# from bs4 import BeautifulSoup
# from urllib.request import urlopen

# url = "https://apps.shopline.com/sort/?type=0&currentPage="
# file = urlopen(url)
# html = file.read()
# soup = BeautifulSoup(html,'html.parser')
# print(soup.prettify)
# # dv = soup.find_all("div")
# # print(dv)

import requests
from bs4 import BeautifulSoup

url = 'https://www.shopline.com/contact-us'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
dv = soup.find("div")
print(soup)
print("--------------------")
print(dv)