# import pandas as pd
# ls = [1, 2, 3]
# lst = []
# for i in ls:
#     inner_list = []
#     for j in range(1, 4):
#         inner_list.append(j)
#     lst.append(inner_list)

# print(lst)
# print(len(lst))

# df = pd.DataFrame({'Lines': [" --> ".join([str(element) for element in sublist]) for sublist in lst]})
# # print(df)

# df.to_excel("trykaro.xlsx",index=False)

# # for d in range(len(lst)):
# #     df = pd.DataFrame({'Lines': [" --> ".join(lst[d])]})
# #     print(df)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd

# review=[]
# reviewdriver = webdriver.Chrome()
# reviewdriver.get("https://apps.shopline.com/detail/?appHandle=variant_combination")
# reviews = reviewdriver.find_elements(By.XPATH,".//div[@class = '_comment_1085k_1']")
# reviews_texts = [reviews.text for reviews in reviews]
# inner=[]
# for text in reviews_texts:
#     inner.append(text)
# review.append(inner)
# # print(review)
# print(len(review))
# df = pd.DataFrame({'Lines': [" --> ".join([str(element) for element in sublist]) for sublist in review]})
# # print(df)
# df.to_excel("smart.xlsx",index=False)


'''
# It is use for scrap title name data from website

from bs4 import BeautifulSoup
import requests

url = "https://www.waleedtoys.com/BrandList?cid=Ki3bgiSxO3vQ6MnH4WXcXXSbegSfsseiyny0"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, "html.parser")

toy_titles = soup.select("div.product-th div.product-dtl h3")
for title in toy_titles:
    value = title.text.strip()
    print(value)
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

appurl = [
    "https://www.waleedtoys.com/ProductDetails?uid=1N6ZTdl41M1lqlKXKLLapOimzCTi7n73Q8JI",
    "https://www.waleedtoys.com/ProductDetails?uid=IuRgIa0wkr33umxragmKV7YMBNjT2wodC4mr"
]

titlelst=[]
desclst = []
stocklst = []
reviewslst = []
item_numberlst = []
yearlst = []
pricelst = []
sizelst =[]
for i in appurl:
    file = urlopen(i)
    html = file.read()
    soup = BeautifulSoup(html,"html.parser")
    response = requests.get(i)
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
'''
import pandas as pd
from bs4 import BeautifulSoup
import requests

base_url = "https://www.waleedtoys.com"
url = "https://www.waleedtoys.com/BrandList?cid=Ki3bgiSxO3vQ6MnH4WXcXXSbegSfsseiyny0"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, "html.parser")

product_titles = []
product_titles.extend([title.text.strip() for title in soup.select("div.product-th div.product-dtl h3")])

# Create a pandas DataFrame with a single column
# df = pd.DataFrame({"Product Titles": product_titles})
print({"Product Titles": product_titles})
# Save the DataFrame to an Excel file
# df.to_excel("view_more_products.xlsx", index=False)



# titlelst=["Balls"]
# desclst = ["Value Pack of colorful small mini play balls for your children's ball pit, play tent, crawl tunnel, playhouse, playpen, bounce house, swimming pool, or bathtub Phthalate, BPA,  toy balls are super safe, super soft, and super fun! You will get eight beautiful colors to keep the kids captivated while rolling around playing kiddie games. Blue, Yellow, Green, Red, Orange, Purple, Pink, and Turquoise Playz is the only brand of pit balls that are turbo-polished around the edges of the balls for a clean, soft finish so your child's delicate skin doesn't get cut. When the balls get dirty, Playz's innovative design allows you to simply toss them in the washer on the cold setting with a non-bleach detergent to rid them of any harmful bacteria. Ball Size : 4.5cm *50 Balls/ Net bag /0157cbm"]
# stocklst = ["In Stock"]
# reviewslst = ["Reviews (0)"]
# item_numberlst = ["SBCCB-02"]
# yearlst = ["Age: Unisex 3+"]
# pricelst = ["2.900 kd"]
# sizelst =[]
# df = pd.DataFrame({"Toy Titles": [", ".join(sizelst)]})
# df.to_excel("size.xlsx",index=False)
