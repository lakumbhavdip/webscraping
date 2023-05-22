from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd
urls = []
url = 'https://www.waleedtoys.com/BrandList?cid=Ki3bgiSxO3vQ6MnH4WXcXXSbegSfsseiyny0'
file = urlopen(url)
html = file.read()
soup = BeautifulSoup(html, "html.parser")

apps = soup.select("div.row.product-listing div.col-lg-3.col-md-3.col-sm-6.product-column div.product-th div.product-card a[href]")
ln = len(apps)
# print(ln)
for i in range(ln):
    if i%2==0:
        # print(i)
        if apps:
            urls.append(apps[i]['href'])
     
titlelst=[]
desclst = []
stocklst = []
reviewslst = []
item_numberlst = []
yearlst = []
pricelst = []
sizelst =[]
for j in urls:
    print(j)
    appurl = "https://www.waleedtoys.com/" + j
    file = urlopen(appurl)
    html = file.read()
    soup = BeautifulSoup(html,"html.parser")
    response = requests.get(appurl)
    html1 = response.content
    soup1 = BeautifulSoup(html1, "html.parser")


    title = soup.find("div",class_="product-detail-right").find("h2").text.strip()
    desc =  soup.find("div",class_="pdesc").text.strip()
    stock =  soup.find("span",class_="alert-success").text.strip()
    reviews =  soup.find("a",class_="reviews-link").find("strong").text.strip()
    item_number = soup.select_one('div.pdesc strong').next_sibling.strip()
    year =  soup.find("span",class_="years-div").text.strip()
    price =  soup.find("span",id="ContentPlaceHolder1_spnDiscountUnitPrice").text.strip()
    sizes = soup1.select("div.product-size li label strong")
    
    titlelst.append(title)
    # print("Title - " ,title)
    desclst.append(desc)
    # print("Descriptions - " ,desc)
    stocklst.append(stock)
    # print("Stock - " ,stock)
    reviewslst.append(reviews)
    # print("Reviews - " ,reviews)
    item_numberlst.append(item_number)
    # print("Item Number - " ,item_number)
    yearlst.append(year)
    # print("Age - " ,year)
    pricelst.append(price)
    # print("Price - " ,price)
    szlst=[]
    for sz in sizes:
        size = sz.text.strip()
        szlst.append(size)
        # print("Size - " ,size) 
    sizelst.append(szlst)
        # print("Size - " ,size)  
    print("-------------------------------------------------------------------------------------------------------------------------------------------")

df = pd.DataFrame({
    "Title - " : titlelst,
   "Descriptions - " :desclst,
   "Stock - " :stocklst,
    "Reviews - " :reviewslst,
    "Item Number - " :item_numberlst,
    "Age - " :yearlst,
   "Price - " :pricelst,
   "Size - " : sizelst
})
df.to_excel("size.xlsx", index=False)

# print(titlelst)
# print(desclst)
# print(stocklst)
# print(reviewslst)
# print(item_numberlst)
# print(yearlst)
# print(pricelst)
# print(sizelst)
    
'''    
appurl = "https://www.waleedtoys.com/ProductDetails?uid=1N6ZTdl41M1lqlKXKLLapOimzCTi7n73Q8JI"
file = urlopen(appurl)
html = file.read()
soup = BeautifulSoup(html,"html.parser")
response = requests.get(appurl)
html1 = response.content
soup1 = BeautifulSoup(html1, "html.parser")


title = soup.find("div",class_="product-detail-right").find("h2").text.strip()
desc =  soup.find("div",class_="pdesc").text.strip()
stock =  soup.find("span",class_="alert-success").text.strip()
reviews =  soup.find("a",class_="reviews-link").find("strong").text.strip()
item_number = soup.select_one('div.pdesc strong').next_sibling.strip()
year =  soup.find("span",class_="years-div").text.strip()
price =  soup.find("span",id="ContentPlaceHolder1_spnDiscountUnitPrice").text.strip()
sizes = soup1.select("div.product-size li label strong")
print("Title - " ,title)
print("Descriptions - " ,desc)
print("Stock - " ,stock)
print("Reviews - " ,reviews)
print("Item Number - " ,item_number)
print("Age - " ,year)
print("Price - " ,price)
for sz in sizes:
    size = sz.text.strip()
    print("Size - " ,size)  
'''