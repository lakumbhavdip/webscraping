from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests
import pandas as pd

# App name, developer name, email, rating, review with pagination


url = "https://appexchange.salesforce.com/appxStore?type=App"
# file = urlopen(webpageAddress)
# html = file.read()
re = requests.get(url)

soup = BeautifulSoup(re.content,'html.parser')

# title = soup.title.get_text()
# print(title)

app = soup.find_all('span',class_="appx-tile-content-el")
# text = re.sub(r'<.*?>', '', str(app))
ls = [
    "Lightning Ready",
    "Professional & Up",
    "Native App",
    "Essentials & Up",
    "Salesforce1 Mobile",
    "Enterprise & Up",
    "No Limits"
]
for i in app:
    if i.text in ls:
        continue
    else:
        print(i.text)

# ls = [title,text]
# print(ls)
# df = pd.DataFrame(ls)
# df.to_excel('scrapdata2.xlsx') 


