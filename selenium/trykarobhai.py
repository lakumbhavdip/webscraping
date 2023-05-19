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

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

review=[]
reviewdriver = webdriver.Chrome()
reviewdriver.get("https://apps.shopline.com/detail/?appHandle=variant_combination")
reviews = reviewdriver.find_elements(By.XPATH,".//div[@class = '_comment_1085k_1']")
reviews_texts = [reviews.text for reviews in reviews]
inner=[]
for text in reviews_texts:
    inner.append(text)
review.append(inner)
# print(review)
print(len(review))
df = pd.DataFrame({'Lines': [" --> ".join([str(element) for element in sublist]) for sublist in review]})
# print(df)
df.to_excel("smart.xlsx",index=False)

