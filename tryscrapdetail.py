# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# import requests


# # def getapps():
# #     webpageAddress = "https://www.shopline.com/contact-us"
# #     html = requests.get(webpageAddress).content
# #     # print(html)
# #     soup = BeautifulSoup(html,"html.parser")
# #     c = soup.find('p', {"class":"paragraph_body-p2 gray contact"})
# #     # print(c)
# #     for row in c:
# #         print(row.getText())
# # contact = getapps()
# # print(contact)        

# # Send a GET request to the website and retrieve the HTML content


# # Find all the application names using the appropriate CSS selector
# # app_names = soup.select('.app-list__item .app-list__title')
# # print(app_names)
# # Extract the text of each application name
# # app_names = [name.get_text(strip=True) for name in app_names]

# # # Print the application names
# # for name in app_names:
# #     print(name)
# # appv = soup.find_all("h4",class_="title_3 color_black1 _appName_warp_1wuz5_34")
# # print(appv)
# # # <h4 class="title_3 color_black1 _appName_warp_1wuz5_34" style="margin-bottom: 2px;">Design maker for campaigns</h4>


# # def getapps():
# #     webpageAddress = "https://apps.shopline.com/sort/?type=0&currentPage=1"
# #     html = requests.get(webpageAddress).content
# #     # print(html)
# #     soup = BeautifulSoup(html,"html.parser")
# #     c = soup.find('h4', {"class":"title_3 color_black1 _appName_warp_1wuz5_34"})
# #     print(c)
# #     # for row in c:
# #     #     print(row.getText())
# # app = getapps()
# # print(app)  

# # from bs4 import BeautifulSoup
# # import requests

# # url = 'https://apps.shopline.com/'
# # file = urlopen(url)
# # html = file.read()
# # soup = BeautifulSoup(html,'html.parser')
# # name = soup.find_all("div").findChildren
# # print(name)


# # import requests
# # from bs4 import BeautifulSoup

# # url = "https://apps.shopline.com/detail/?appHandle=zhekouhuodongsh"

# # response = requests.get(url)
# # soup = BeautifulSoup(response.content, "html.parser")

# # # app_title = soup.find("h1", class_="detail--apps--title")
# # # developer_name = soup.find("a", class_="detail--apps--developer")
# # # description = soup.find("div", class_="detail--apps--description")
# # description = soup.find("div", class_="self_adaption_warp _appsort_content_warp_1b5ii_1")

# # # print("App Title:", app_title)
# # # print("Developer Name:", developer_name)
# # # print("Description:", description)
 
 
# import requests
# from bs4 import BeautifulSoup


# response = requests.get('https://apps.shopline.com/sort/?type=0&currentPage=1')

# soup = BeautifulSoup(response.content, 'html.parser')

# print(soup.prettify())


# import requests
# from bs4 import BeautifulSoup

# # URL of the page to scrape
# url = "https://appexchange.salesforce.com/appxStore?type=App"

# # Send a GET request to the URL
# response = requests.get(url)

# # Create BeautifulSoup object with the response content
# soup = BeautifulSoup(response.content, 'html.parser')

# # Find all div elements with class "tile-text"
# tiles = soup.find("span", class_="appx-tile-content-el")
# print(tiles)

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

# base_url = 'https://apps.shopline.com/sort/?type=0&currentPage='
# page = 1
# application_names = []

# while True:
#     url = base_url + str(page)
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     # Find all the application names on the page
#     names = soup.find_all('h4', class_='title_3 color_black1 _appName_warp_1wuz5_34')
#     print(names)
#     # If no names are found, break the loop
#     if len(names) == 0:
#         break
    
#     # Extract the text of each application name and append it to the list
#     for name in names:
#         application_names.append(name.text.strip())
    
#     page += 1

# Print all the application names
# for name in application_names:
#     print(name)

# print("------------------------------------------------------------------------------------------------------------------------")

# webadd = "https://udyamregistration.gov.in/Government-India/Ministry-MSME-registration.htm"
# file = urlopen(webadd)
# html = file.read()
# # req = requests.get(webadd)
# soup = BeautifulSoup(html,'html.parser')
# head = soup.find("div",class_="section-title").find("h2")
# prgp = soup.find("div",class_="section-title").find("p")
# print(head.get_text())
# print("------------------------------------------------------------------------------------------------------------------------")
# print(prgp.get_text())



# print("------------------------------------------------------------------------------------------------------------------------")
# 16-5-2023

# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# webpageAddress = "https://apps.shopline.com/detail/?appHandle=zhekouhuodongsheji"
# file = urlopen(webpageAddress)
# html = file.read().decode('utf-8')
# soup = BeautifulSoup(html, 'html.parser')
# # print(soup.prettify())
# dv= soup.find("div",class_="_Appdetail_warp_rlnwk_1")
# print(dv)

