from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

chargelst=[]
reviewlst=[]

ls = []
for i in range(1,8):
    s = str(i)
    url = (f"https://apps.shopline.com/sort/?pricing=all&type=0&appName=&strategy=appPopular&currentPage={s}")
    # print(url)   
    ls.append(url)

for i in ls:
    
    driver = webdriver.Chrome()
    driver.get(i)
    review = driver.find_elements(By.XPATH, ".//div[@class='_appStarItem_1bki9_1']")
    # print(title)
    # Convert the elements to text format
    review_texts = [review.text for review in review]
    # Print the converted text
    for text in review_texts:
        # print(text)
        reviewlst.append(text)
        
    charge = driver.find_elements(By.XPATH, ".//span[@class='body_4 color_black1']")
    # print(title)
    # Convert the elements to text format
    charge_texts = [charge.text for charge in charge]
    # Print the converted text
    for text1 in charge_texts:
        # print(text)
        chargelst.append(text1)
    driver.close

print("------------------------------------------------------------------------------------------------------------")

# df = pd.DataFrame(reviewlst)
# print(df)
# df.to_excel("reviews.xlsx",index=False)

# df1 = pd.DataFrame(chargelst)
# print(df1)
# df1.to_excel("charge.xlsx",index=False)