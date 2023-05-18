from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd

webpageAddress = "https://apps.shopline.com/sort/?type=0&currentPage=1"
file = urlopen(webpageAddress)
html = file.read()
soup = BeautifulSoup(html,'html.parser')
# print(soup.prettify())
title = soup.title.get_text()

sd = [title]
webpageAddress = "https://www.shopline.com/contact-us"
html = requests.get(webpageAddress).content
# print(html)
soup = BeautifulSoup(html,"html.parser")
# print(soup.prettify())
c = soup.find('p', {"class":"paragraph_body-p2 gray contact"})
# print(c)
ls = []
for row in c:
    ne = row.getText()
    # print(ne)
    ls.append(ne)
    # print(ls)
for i in ls:
    sd.append(i)

print(sd)

# df = pd.DataFrame(sd)
# print(df)
# df.to_excel('scrapdata.xlsx')

