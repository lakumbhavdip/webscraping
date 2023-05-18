#find a user are enter a city and is city's petrol and diesal price catch

from bs4 import BeautifulSoup
from urllib.request import urlopen
city=input("enter a city'sname ")

WebPageAddress = (f"https://www.creditmantri.com/diesel-price-in-{city}/")

file = urlopen(WebPageAddress)
html = file.read()

soup = BeautifulSoup(html,'html.parser')

prices=soup.body.find('div',{'class':'col-sm-8 col-xs-8 text-center'})
for price in prices:
    print(price.get_text())
