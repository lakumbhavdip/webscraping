# # from requests_html import HTMLSession

# # url = "https://apps.shopline.com/sort/?type=0&currentPage="

# # s = HTMLSession()
# # r =s.get(url)
# # r.html.render(sleep=1)

# # apps = r.html.xpath('//*[@class= "_applist_content_warp_1wuz5_1"]')
# # print(apps)
# import pandas as pd


# # Create a list with multiple lines or indices
# my_list = ['Line 1', 'Line 2', 'Line 3']

# # Create a new DataFrame with a single cell
# df = pd.DataFrame({'Lines': [" ".join(my_list)]})

# # Export the DataFrame to an Excel file
# df.to_excel('output.xlsx', index=False)


import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Set up Chrome WebDriver with Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_service = Service("path/to/chromedriver")  # Replace with actual path to chromedriver executable
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

url = "https://www.waleedtoys.com/BrandList?cid=Ki3bgiSxO3vQ6MnH4WXcXXSbegSfsseiyny0"
driver.get(url)

# Click the "View More" button repeatedly until all products are loaded
while True:
    try:
        view_more_button = driver.find_element(By.CSS_SELECTOR, "a.btn-load-more")
        view_more_button.click()
    except:
        break

# Extract the product titles
product_titles = driver.find_elements(By.CSS_SELECTOR, "div.product-th div.product-dtl h3")
product_titles = [title.text.strip() for title in product_titles]

# Create a pandas DataFrame with a single column
df = pd.DataFrame({"Product Titles": product_titles})
print(df)
# Save the DataFrame to an Excel file
# df.to_excel("view_more_products.xlsx", index=False)

# Quit the WebDriver
driver.quit()
