from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

appname=[]
ls = []
for i in range(1,8):
    s = str(i)
    url = (f"https://apps.shopline.com/sort/?pricing=all&type=0&appName=&strategy=appPopular&currentPage={s}")
    # print(url)   
    ls.append(url)
    
# print(ls)
for i in ls:
    # print(i)
    
    driver = webdriver.Chrome()
    driver.get(i)
    title = driver.find_elements(By.XPATH, ".//*[@class='title_3 color_black1 _appName_warp_1wuz5_34']")
    # print(title)
    # Convert the elements to text format
    title_texts = [title.text for title in title]
    # Print the converted text
    for text in title_texts:
        print(text)
        appname.append(text)
    driver.close
print("------------------------------------------------------------------------------------------------------------")
# print(appname)
# df = pd.DataFrame(appname)
# df.to_excel('appname.xlsx') 

#================================================================================================================================
# lp= list(driver.find_elements(By.XPATH, ".//*[@rel='nofollow']"))
# # Extract the text from the elements
# lt = [l.text for l in lp]

# for l in lt:
#     s = str(l)
#     print(s)


# version fetch karvanu chhe e kya chhe
#================================================================================================================================
    
# nb = driver.find_elements(By.XPATH, ".//*[@class='ant-pagination-next']") 





from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

appname=[]
for i in range(1,8):
    s = str(i)
    url = (f"https://apps.shopline.com/sort/?pricing=all&type=0&appName=&strategy=appPopular&currentPage={s}")
    # print(url)   
    
# print(ls)
for i in url:
    # print(i)
    
    driver = webdriver.Chrome()
    driver.get(i)
    title = driver.find_elements(By.XPATH, ".//[@class='title_3 color_black1 _appName_warp_1wuz5_34']")
    # print(title)
    # Convert the elements to text format
    title_texts = [title.text for title in title]
    # Print the converted text
    for text in title_texts:
        print(text)
        appname.append(text)
    driver.close